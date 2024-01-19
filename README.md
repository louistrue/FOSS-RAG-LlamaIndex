# LlamaIndex: Advanced Opensource Data Retrieval and Analysis 📘

## Acknowledgments 👏
first seen [here at LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/low_level/oss_ingestion_retrieval.html) 😍.

Special thanks to the teams behind `LlamaIndex` components, `HuggingFace` for embedding models, `PyMuPDF` for document parsing, and `PostgreSQL` for database management.

## Table of Contents
- [Introduction 🌟](#introduction-)
- [Features 🚀](#features-)
- [Installation 🔧](#installation-)
  - [Preparing Python Environment](#preparing-python-environment)
  - [Troubleshooting Common PostgreSQL Issues](#troubleshooting-common-postgresql-issues)
- [Detailed Usage Guide 📊](#detailed-usage-guide-)
  - [Initial Setup](#initial-setup)
  - [Document Loading and Processing](#document-loading-and-processing)
  - [Model Selection and Embedding](#model-selection-and-embedding)
  - [Database Interaction](#database-interaction)
  - [Querying and Retrieval](#querying-and-retrieval)
- [Configuration Settings ⚙️](#configuration-settings-)
- [PostgreSQL Quick Start 🐘](#postgresql-quick-start-)
  - [Intro to `psql`](#intro-to-psql)
  - [Basic PostgreSQL Commands](#basic-postgresql-commands)
  - [Adding Extensions to a Database](#adding-extensions-to-a-database)
- [RAG Implementation Insights with LlamaIndex 🧠](#rag-implementation-insights-with-llamaindex-)
  - [Overview](#overview)
  - [Components of RAG in LlamaIndex](#components-of-rag-in-llamaindex)
  - [Deep Dive into Process](#deep-dive-into-process)
  - [Challenges and Improvements](#challenges-and-improvements)
  - [Additional Resources](#additional-resources)
- [Videos ▶️](#videos-)

## Introduction 🌟
**LlamaIndex** is a data retrieval and analysis tool to for process and query large text datasets with advanced machine learning models and database technologies using RAG (Retrieval-Augmented Generation).

## Features 🚀
- **Data Processing 🔄**: Efficient document loading with `PyMuPDFReader`, and optimized data handling using `SentenceSplitter`.
- **Advanced Query Capabilities 🔍**: Deep text understanding with `LlamaCPP`, and natural language querying via `QueryBundle`.
- **Flexible Data Storage 🗃️**: Effective vector management in PostgreSQL databases with `PGVectorStore`.
- **Command Line Interface 🌐**: Simplified command-line interface with clear operation logging.

## Installation 🔧
- **Environment Configuration 🌍**: Set up `LLAMA_MODEL_PATH`, `DOCUMENT_PATH`, `DB_PASSWORD`.
- **Database Initialization 🛠️**: Initialize PostgreSQL with `PGVectorStore`, and connect using `psycopg2`.

### Preparing Python Environment
Install `psycopg2` with `pip install psycopg2` for PostgreSQL interaction in Python.

### Troubleshooting Common PostgreSQL Issues
- **Connection Issues**: Check server status, credentials, and firewall settings.
- **Performance Bottlenecks**: Analyze queries with `EXPLAIN` and optimize indexing.
- **Locks and Deadlocks**: Monitor and manage database locks.

## Detailed Usage Guide 📊

### Initial Setup
Install necessary Python packages, set up environment variables, and configure PostgreSQL.

### Document Loading and Processing
1. Load documents using `PyMuPDFReader`.
2. Parse text with `SentenceSplitter`.

### Model Selection and Embedding
- Experimented with various models on Hugging Face, including `BAAI/bge-small-en-v1.5` and `dbmdz/bert-base-german-cased`.
- Final selection: `TheBloke/em_german_leo_mistral-GGUF` for German content.
- Switch models in `HuggingFaceEmbedding` instantiation.

### Database Interaction
- Initialize PostgreSQL database and connect using `psycopg2`.
- Manage document embeddings with `PGVectorStore`.

### Querying and Retrieval
1. Write your query as a string.
2. Generate query embeddings.
3. Retrieve and rank documents with `VectorDBRetriever` and `RetrieverQueryEngine`.

## Configuration Settings ⚙️
- **LlamaCPP Model Settings**: `model_path`, `temperature`, `max_new_tokens`, `context_window`, `model_kwargs`.
- **Database Connection Settings**: `db_name`, `host`, `password`, `port`, `user`.
- **Vector Store Configuration**: `table_name`, `embed_dim`.
- **Document Processing and Query Settings**: `chunk_size`, `similarity_top_k`.

## PostgreSQL Quick Start 🐘

### Intro to `psql`
- Start with `psql -U username -d dbname`.
- Connect to a database with `\c dbname`.
- Execute SQL files with `\i path/to/file.sql`.
- Exit with `\q`.

### Basic PostgreSQL Commands
- Create/Delete Database: `CREATE DATABASE dbname;`, `DROP DATABASE dbname;`
- Create User: `CREATE USER username WITH PASSWORD 'password';`
- Grant Privileges: `GRANT ALL PRIVILEGES ON DATABASE dbname TO username;`
- List Databases/Tables: `\l`, `\dt`
- Display Table Structure: `\d tablename`
- Run a Query: `SELECT * FROM tablename;`

### Adding Extensions to a Database
```sql
CREATE EXTENSION IF NOT EXISTS PGVectorStore;
```

## RAG Implementation Insights with LlamaIndex 🧠

### Overview
Retrieval-Augmented Generation (RAG) in LlamaIndex enhances data retrieval with a combination of retrieval-based and generative AI models.

### Components of RAG in LlamaIndex
1. **Retrieval System**: Uses `PGVectorStore` for vector-based retrieval.
2. **Generative System**: Uses models like `LlamaCPP` for generating coherent responses.

### Process Overview 
1. Document Chunking and Embedding with `SentenceSplitter` and `HuggingFaceEmbedding`.
2. Query Processing: Embed queries and match with document embeddings.
3. Contextualization and Generation with `LlamaCPP`.

### Challenges and Improvements
1. **Chunk Size Optimization**: Explore different chunk sizes.
2. **Contextual Metadata Enhancement**: Add semantic tags and thematic links.
3. **Model Experimentation and Tuning**: Continue exploring models for multilingual content.

### Additional Resources
- [Building Performant RAG Applications for Production by LlamaIndex](https://docs.llamaindex.ai/en/stable/optimizing/production_rag.html)
- [Routers by LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/querying/router/root.html)

## Videos ▶️
- [Jerry Liu–LlamaIndex – Practical Data Considerations for building Production-Ready LLM Applications](https://youtu.be/g-VvYLhYhOg?si=oHzKibrdste4XQWF)
- [Building Production-Ready RAG Applications: Jerry Liu](https://youtu.be/TRjq7t2Ms5I?si=eZYRhZVE1eJSl8Ve)
- [High-performance RAG with LlamaIndex](https://www.youtube.com/live/wBhY-7B2jdY?si=7AxHoos8vbPVpvOe)
- [Lessons Learned on LLM RAG Solutions](https://www.youtube.com/live/Y9qn4XGH1TI?si=h51EGDBvWYFZyxvu)
```
