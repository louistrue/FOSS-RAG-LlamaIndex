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
- **Database Initialization 🛠️**: Steps to initialize and configure PostgreSQL database, and establish connections using `psycopg2`.

Absolutely, I'll include information about the `\c` command for connecting to a database in `psql` and mention the prerequisite of installing `psycopg2` for Python interaction with PostgreSQL.


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
CREATE EXTENSION IF NOT EXISTS extension_name;
```
Replace `extension_name` with the desired extension's name.

### Preparing Python Environment
Before interacting with PostgreSQL in Python:
- **Install `psycopg2`**: Run `pip install psycopg2` in your Python environment. This library enables Python applications to connect to PostgreSQL.

### Tips for Working with PostgreSQL in Python
- Use `psycopg2` for executing SQL commands and managing database connections in Python.

### Troubleshooting Common PostgreSQL Issues
- **Connection Issues**: Check server status, credentials, and firewall settings.
- **Performance Bottlenecks**: Use `EXPLAIN` for query analysis and optimize with indexing.
- **Locks and Deadlocks**: Monitor and manage database locks.


## Usage Guide 📊
- **Loading Documents 📄**: Data loading and preprocessing for analysis.
- **Querying Data 📊**: embedding & indexing data with `HuggingFaceEmbedding`, and querying with `RetrieverQueryEngine`.
- **Retrieving Results 📈**: query results and access node information.

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

## License 📜
This project is licensed under [tbd].

## Acknowledgments 👏
seen [here](https://docs.llamaindex.ai/en/stable/examples/low_level/oss_ingestion_retrieval.html) 😍.

Special thanks to the teams behind `LlamaIndex` components: `HuggingFace` for embedding models, `PyMuPDF` for document parsing, and `PostgreSQL` for database management. 
