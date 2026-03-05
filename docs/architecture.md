# RepoSage Architecture

## Overview

RepoSage is a full stack AI-powered developer tool that helps engineers understand large codebases more quickly.

Large repositories can contain thousands of files and hundreds of thousands of lines of code. Developers often struggle to:

- locate where a feature is implemented
- understand interactions between components
- trace bugs across multiple files
- explore unfamiliar codebases

RepoSage solves this problem by combining:

- repository indexing
- keyword search
- semantic search using embeddings
- Retrieval Augmented Generation (RAG)

The system analyzes a repository, stores a semantic representation of the code, and allows developers to ask questions about how the system works.

Example questions include:

- Where is authentication implemented?
- Which files handle database connections?
- What part of the code sends emails?
- How does the login flow work?

RepoSage retrieves relevant code segments and uses an AI model to generate explanations grounded in the actual repository code.

---

## High Level Architecture

RepoSage consists of four main components:

1. Frontend Application
2. Backend API
3. Database and Vector Storage
4. AI Model Services

Data flows through the system in the following way:

User
↓
Next.js Frontend
↓
FastAPI Backend
↓
PostgreSQL + pgvector
↓
Embedding API
↓
Language Model API

---

## Frontend

The frontend is built using **Next.js** and provides the user interface for interacting with RepoSage.

The frontend allows users to:

- upload repository ZIP files
- browse repository files
- search code using keywords
- perform semantic search
- ask questions about the codebase
- view AI generated explanations with code references

Technologies used:

- Next.js
- React
- Tailwind CSS

The frontend communicates with the backend through REST API requests.

---

## Backend

The backend is implemented using **FastAPI** and handles all core application logic.

Responsibilities of the backend include:

- receiving repository uploads
- extracting repository contents
- parsing and storing source files
- performing keyword search
- generating embeddings for code chunks
- performing vector similarity search
- executing the RAG pipeline for question answering
- running evaluation metrics

The backend exposes several API endpoints that the frontend interacts with.

Examples include:

GET /health
POST /upload-zip
GET /search
POST /semantic-search
POST /ask

---

## Database

RepoSage uses **PostgreSQL with the pgvector extension**.

The database stores:

- repository metadata
- file contents
- code chunks
- embedding vectors
- question history
- evaluation results

pgvector enables efficient similarity search between embedding vectors.

This allows the system to retrieve the most relevant code segments for a given question.

---

## AI Components

RepoSage uses several AI concepts to enable intelligent repository understanding.

### Embeddings

Code chunks are converted into embedding vectors that represent their semantic meaning.

These embeddings allow the system to find similar code even when exact keywords do not match.

Example:

Query:

"Where is login implemented?"

The system may retrieve code related to:

- authentication
- session creation
- password verification

even if the word "login" is not used.

---

### Vector Search

When a user submits a query:

1. The query is converted into an embedding vector.
2. The system compares this vector with stored code embeddings.
3. The most similar code chunks are retrieved.

This process is called **vector similarity search**.

---

### Retrieval Augmented Generation (RAG)

RAG combines retrieval with language model generation.

Instead of asking a language model to answer from its training data, RepoSage provides relevant code context.

The process works as follows:

1. User submits a question.
2. Semantic search retrieves relevant code chunks.
3. The system constructs a prompt containing the question and code context.
4. The prompt is sent to a language model.
5. The language model generates an explanation grounded in the provided code.

This approach significantly reduces hallucinations and improves answer accuracy.

---

## System Workflow

The overall workflow of RepoSage is as follows:

1. User uploads a repository ZIP file.
2. The backend extracts and reads repository files.
3. Supported source files are processed.
4. Files are split into smaller code chunks.
5. Embeddings are generated for each chunk.
6. Embeddings are stored in the vector database.
7. Users can search the repository using keywords or semantic queries.
8. When a question is asked, relevant code chunks are retrieved.
9. A language model generates an explanation using those code snippets.
10. The explanation and code references are returned to the user.

---

## Future Improvements

Potential future improvements include:

- authentication and user accounts
- repository history tracking
- incremental repository updates
- improved code chunking strategies
- caching frequently asked questions
- streaming AI responses
- improved evaluation pipelines

These enhancements would allow RepoSage to scale into a production grade developer tool.
