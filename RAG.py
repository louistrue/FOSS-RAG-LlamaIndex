import os
from pathlib import Path
import psycopg2
from sqlalchemy import make_url
from typing import Any, List, Optional

from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.llms import LlamaCPP
from llama_index import ServiceContext, QueryBundle
from llama_index.vector_stores import PGVectorStore, VectorStoreQuery
from llama_index.node_parser.text import SentenceSplitter
from llama_index.schema import TextNode, NodeWithScore
from llama_index.retrievers import BaseRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_hub.file.pymu_pdf.base import PyMuPDFReader

from dotenv import load_dotenv
load_dotenv()  

# Loading environment variables
MODEL_PATH = os.getenv('LLAMA_MODEL_PATH')
DOCUMENT_PATH = os.getenv('DOCUMENT_PATH')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Embedding model
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
#embed_model = HuggingFaceEmbedding(model_name="dbmdz/bert-base-german-cased")
#embed_model = HuggingFaceEmbedding(model_name="timpal0l/mdeberta-v3-base-squad2")


# LlamaCPP Model (em_german_leo_mistral.Q5_K_M.gguf)
llm = LlamaCPP(
    model_path=MODEL_PATH,
    temperature=0.15,
    max_new_tokens=1000,
    context_window=8000,
    generate_kwargs={},
    model_kwargs={"n_gpu_layers": 33},
    verbose=True,
)

service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)

# Database connection
db_name = "vector_db"
host = "localhost"
password = DB_PASSWORD
port = "5432"
user = "postgres"
conn = psycopg2.connect(dbname="postgres", host=host, password=password, port=port, user=user)
conn.autocommit = True

with conn.cursor() as c:
    c.execute(f"DROP DATABASE IF EXISTS {db_name}")
    c.execute(f"CREATE DATABASE {db_name}")

# Vector store
vector_store = PGVectorStore.from_params(
    database=db_name,
    host=host,
    password=password,
    port=port,
    user=user,
    table_name="llama2_paper",
    embed_dim=384
    #embed_dim=768,
)

# Document loading and parsing
loader = PyMuPDFReader()
documents = loader.load(file_path=DOCUMENT_PATH)

text_parser = SentenceSplitter(chunk_size=2000) #512
text_chunks = []
doc_idxs = []
for doc_idx, doc in enumerate(documents):
    cur_text_chunks = text_parser.split_text(doc.text)
    text_chunks.extend(cur_text_chunks)
    doc_idxs.extend([doc_idx] * len(cur_text_chunks))

nodes = []
for idx, text_chunk in enumerate(text_chunks):
    node = TextNode(text=text_chunk)
    src_doc = documents[doc_idxs[idx]]
    node.metadata = src_doc.metadata
    nodes.append(node)

for node in nodes:
    node_embedding = embed_model.get_text_embedding(node.get_content(metadata_mode="all"))
    node.embedding = node_embedding

vector_store.add(nodes)

# Query processing
#query_str = "Erklaere detailliert die Grundlagen zu Tragsicherheit"
#query_str = "Definiere: Universal-Keilzinkenverbindung"
#query_str = "What is Balkenschichtholz?"
query_str = "Please explain the concept of Robustheit/robustness"
#query_str = "Please explain the concept of Holzfeuchte/moisture content in detail"

query_embedding = embed_model.get_query_embedding(query_str)
vector_store_query = VectorStoreQuery(
    query_embedding=query_embedding, similarity_top_k=2, mode="default"
)
query_result = vector_store.query(vector_store_query)

print(query_result.nodes[0].get_content())


# Retriever implementation
class VectorDBRetriever(BaseRetriever):
    def __init__(self, vector_store: PGVectorStore, embed_model: Any, query_mode: str = "default", similarity_top_k: int = 2) -> None:
        self._vector_store = vector_store
        self._embed_model = embed_model
        self._query_mode = query_mode
        self._similarity_top_k = similarity_top_k
        super().__init__()

    def _retrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
        query_embedding = self._embed_model.get_query_embedding(query_bundle.query_str)
        vector_store_query = VectorStoreQuery(
            query_embedding=query_embedding,
            similarity_top_k=self._similarity_top_k,
            mode=self._query_mode,
        )
        query_result = self._vector_store.query(vector_store_query)

        nodes_with_scores = []
        for index, node in enumerate(query_result.nodes):
            score: Optional[float] = None
            if query_result.similarities is not None:
                score = query_result.similarities[index]
            nodes_with_scores.append(NodeWithScore(node=node, score=score))
        return nodes_with_scores

retriever = VectorDBRetriever(vector_store, embed_model, query_mode="default", similarity_top_k=2)
query_engine = RetrieverQueryEngine.from_args(retriever, service_context=service_context)
response = query_engine.query(query_str)

print(str(response))