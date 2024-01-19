# FOSS RAG using LlamaIndex: Opensource retrieval augmented generation 📘

## Intro 🌟
**LlamaIndex** is a data retrieval and analysis tool designed for the efficient processing and querying of large text datasets. Utilizing advanced machine learning models and database technologies, it is an interesting solution for anyone seeking to derive insights from complex data.

## Features 🚀
- **Data Processing 🔄**: Efficient document loading and parsing with `PyMuPDFReader`, and optimized data handling using `SentenceSplitter`.
- **Advanced Query Capabilities 🔍**: Deep text understanding with `LlamaCPP`, and natural language querying via `QueryBundle`.
- **Flexible Data Storage 🗃️**: Effective vector management in PostgreSQL databases with `PGVectorStore`.
- **cmd Interface 🌐**: Simplified command-line interface with clear operation logging.

## Installation 🔧
- **Environment Configuration 🌍**: Set up essential environment variables including `LLAMA_MODEL_PATH`, `DOCUMENT_PATH`, `DB_PASSWORD`.
- **Database Initialization 🛠️**Initialize and configure PostgreSQL database with `PGVectorStore`, and establish connections using `psycopg2`.

(see PostgreSQL Quick Start below)

### Preparing Python Environment
Before interacting with PostgreSQL in Python:
- **Install `psycopg2`**: Run `pip install psycopg2` in your Python environment. This library enables Python applications to connect to PostgreSQL.

### Tips for Working with PostgreSQL in Python
- Use `psycopg2` for executing SQL commands and managing database connections in Python.

### Troubleshooting Common PostgreSQL Issues
- **Connection Issues**: Check server status, credentials, and firewall settings.
- **Performance Bottlenecks**: Use `EXPLAIN` for query analysis and optimize with indexing.
- **Locks and Deadlocks**: Monitor and manage database locks.


Certainly! Let's expand the Usage Guide section with more detail, including your experimentation with different models and the transition from the original English-only implementation to using the Hugging Face model `TheBloke/em_german_leo_mistral-GGUF`.

---

# LlamaIndex: Advanced Opensource Data Retrieval and Analysis 📘

## [Previous Sections]

## Detailed Usage Guide 📊

### Initial Setup
Before diving into LlamaIndex, ensure that your environment is correctly set up. This includes installing necessary Python packages, setting up environment variables, and ensuring PostgreSQL is configured and running.

### Document Loading and Processing
1. **Load Documents**: Utilize `PyMuPDFReader` to load documents from the specified `DOCUMENT_PATH`.
2. **Text Parsing**: Apply `SentenceSplitter` to divide the text into manageable chunks for processing.

### Model Selection and Embedding
- **Hugging Face Models**:
  - Originally, LlamaIndex used English-only models for text processing.
  - To expand capabilities, I experimented with various models on the Hugging Face platform. This included models like `BAAI/bge-small-en-v1.5` and `dbmdz/bert-base-german-cased`.
  - The final selection was `TheBloke/em_german_leo_mistral-GGUF`, which improved handling of German-language content and gives very consistent grrman responses. This model can be found [here](https://huggingface.co/TheBloke/em_german_leo_mistral-GGUF).
  - To switch models, simply comment out the current model and uncomment the desired model in the `HuggingFaceEmbedding` instantiation but be aware you will probably have to change Settings...

    ```python
    # embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    embed_model = HuggingFaceEmbedding(model_name="TheBloke/em_german_leo_mistral-GGUF")
    # embed_model = HuggingFaceEmbedding(model_name="dbmdz/bert-base-german-cased")
    ```

### Database Interaction
- **Initialization**: Set up the PostgreSQL database with the required structure and connect using `psycopg2`.
- **Vector Store**: Utilize `PGVectorStore` for managing document embeddings in the database.

### Querying and Retrieval
1. **Formulate Query**: Write your query as a string. This can be in English or German, depending on the chosen model.
2. **Query Embedding**: Generate embeddings for your query using the same model used for document processing.
3. **Retrieval**: Use `VectorDBRetriever` and `RetrieverQueryEngine` to retrieve and rank the most relevant documents based on your query.

## Configuration Settings ⚙️
- **LlamaCPP Model Settings**:
  - `model_path`: Path to the LlamaCPP model.
  - `temperature`: Temperature setting for model inference.
  - `max_new_tokens`, `context_window`: Settings for token generation and context management.
  - `model_kwargs`: Additional model-specific parameters like `n_gpu_layers`.
- **Database Connection Settings**:
  - `db_name`, `host`, `password`, `port`, `user`: PostgreSQL database connection parameters.
- **Vector Store Configuration**:
  - `table_name`, `embed_dim`: Parameters for vector storage and embedding dimensions.
- **Document Processing and Query Settings**:
  - `chunk_size`: Size of text chunks for processing.
  - `similarity_top_k`: Top K settings for similarity scoring in queries.

## Troubleshooting 🛠️
- **Common Issues ⚠️**: Solutions for frequent challenges like database connection errors, model loading issues, and query response discrepancies.

## PostgreSQL Quick Start 🐘

### Intro to `psql`
`psql` is PostgreSQL's command-line tool, providing an interactive and scriptable interface for database management.

- **Starting `psql`**: Execute `psql -U username -d dbname`.
- **Connecting to a Database**: Use `\c dbname` to connect to a specific database.
- **Executing a SQL File**: Run `\i path/to/file.sql`.
- **Exiting `psql`**: Enter `\q` to exit.

### Basic PostgreSQL Commands
- **Creating a Database**: `CREATE DATABASE dbname;`
- **Deleting a Database**: `DROP DATABASE dbname;`
- **Creating a User**: `CREATE USER username WITH PASSWORD 'password';`
- **Granting Privileges**: `GRANT ALL PRIVILEGES ON DATABASE dbname TO username;`
- **Listing Databases**: `\l` or `\list`
- **Listing Tables**: `\dt`
- **Displaying Table Structure**: `\d tablename`
- **Running a Query**: `SELECT * FROM tablename;`

### Adding Extensions to a Database
To enhance PostgreSQL functionality, add extensions using:
```sql
CREATE EXTENSION IF NOT EXISTS ## PostgreSQL Quick Start 🐘

### Intro to `psql`
`psql` is PostgreSQL's command-line tool, providing an interactive and scriptable interface for database management.

- **Starting `psql`**: Execute `psql -U username -d dbname`.
- **Connecting to a Database**: Use `\c dbname` to connect to a specific database.
- **Executing a SQL File**: Run `\i path/to/file.sql`.
- **Exiting `psql`**: Enter `\q` to exit.

### Basic PostgreSQL Commands
- **Creating a Database**: `CREATE DATABASE dbname;`
- **Deleting a Database**: `DROP DATABASE dbname;`
- **Creating a User**: `CREATE USER username WITH PASSWORD 'password';`
- **Granting Privileges**: `GRANT ALL PRIVILEGES ON DATABASE dbname TO username;`
- **Listing Databases**: `\l` or `\list`
- **Listing Tables**: `\dt`
- **Displaying Table Structure**: `\d tablename`
- **Running a Query**: `SELECT * FROM tablename;`

### Adding Extensions to a Database
To enhance PostgreSQL functionality, add extensions using:
```sql
CREATE EXTENSION IF NOT EXISTS PGVectorStore;
```
Replace `extension_name` with the desired extension's name.
;
```
Replace `PGVectorStore` with the desired extension's name.




## RAG Implementation Insights with LlamaIndex

### Overview
Retrieval-Augmented Generation (RAG) is an advanced approach that combines the strengths of retrieval-based and generative AI models. In our LlamaIndex application, RAG plays a pivotal role in enhancing the data retrieval process, enabling more nuanced and contextually relevant responses. 

### Components of RAG in LlamaIndex
1. **Retrieval System**:
   - The retrieval component is crucial for identifying relevant chunks of text from the database that correspond to the query.
   - We employ vector-based retrieval using `PGVectorStore` which stores embeddings of text documents.

2. **Generative System**:
   - The generative aspect, powered by models like `LlamaCPP`, is used to generate coherent and contextually appropriate responses.
   - This component synthesizes information from the retrieved documents to construct a comprehensive answer.

### Deep Dive into Process
1. **Document Chunking and Embedding**:
   - Documents are broken into smaller chunks using `SentenceSplitter`, optimizing for both information density and context continuity.
   - Each chunk is then embedded using a transformer-based model like `HuggingFaceEmbedding`. The choice of the embedding model is crucial as it determines the quality of the vector representations.

2. **Query Processing**:
   - Queries are similarly embedded using the same model to ensure compatibility with the document embeddings.
   - The retrieval system then matches the query embedding with the closest document embeddings, effectively fetching the most relevant chunks.

3. **Contextualization and Generation**:
   - The generative model considers the context provided by the retrieved chunks.
   - It uses this context to generate a response that is not just a regurgitation of the retrieved text but a coherent, synthesized answer, leveraging the generative capabilities of `LlamaCPP`.

### Challenges and Improvements
1. **Chunk Size Optimization**:
   - Currently, the chunk size may not be optimally set, potentially leading to loss of context or retrieval of overly broad content.
   - Experimentation with different chunk sizes could lead to better retrieval performance, ensuring that the most relevant and concise information is retrieved, although this is alreadyworking surprisingly well.

2. **Contextual Metadata Enhancement**:
   - Adding more contextual information to the metadata of each chunk could significantly improve retrieval relevance.
   - This approach might include annotating chunks with additional semantic tags or linking chunks to broader thematic elements.

3. **Model Experimentation and Tuning**:
   - While `TheBloke/em_german_leo_mistral-GGUF` has shown promising results, continuous exploration of different models might uncover more effective solutions, especially for handling multilingual content.

4. Optimizing Context Embeddings, Dynamically Retrieving Chunks Depending on Task, Structured Retrieval and more found [here] (https://docs.llamaindex.ai/en/stable/optimizing/production_rag.html) and [here](https://docs.llamaindex.ai/en/stable/module_guides/querying/router/root.html)

## Videos ▶️

--High-performance RAG with LlamaIndex by AI Makerspace
3500: (https://www.youtube.com/live/wBhY-7B2jdY?si=7AxHoos8vbPVpvOe)

## License 📜
This project is licensed under [tbd].

## Acknowledgments 👏
first seen [here at LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/low_level/oss_ingestion_retrieval.html) 😍.

Special thanks to the teams behind `LlamaIndex` components, `HuggingFace` for embedding models, `PyMuPDF` for document parsing, and `PostgreSQL` for database management. 
