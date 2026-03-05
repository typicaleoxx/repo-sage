# repo-sage

# RepoSage

RepoSage is an AI powered developer tool that helps engineers understand large codebases more quickly.

Large repositories often contain thousands of files and many interconnected components. Developers frequently struggle to locate where features are implemented, understand how different parts of the system interact, and trace the source of bugs.

RepoSage addresses this problem by combining repository indexing, code search, and AI generated explanations.

Users can upload a repository, explore its files, search through the code, and ask questions about how the system works.

Examples of questions a user might ask include:

* Where is authentication implemented?
* Which files handle database connections?
* What part of the code sends emails?
* How does the login flow work?

RepoSage retrieves relevant code segments and generates explanations grounded in the repository itself.

---

# Features

RepoSage will support the following capabilities:

* Upload a repository as a ZIP file
* Browse repository files through a web interface
* Perform keyword search across code
* Perform semantic search using embeddings
* Ask natural language questions about the codebase
* Receive AI generated explanations with references to the code
* Measure answer quality using evaluation metrics

---

# Technology Stack

Frontend

* Next.js
* React
* Tailwind CSS

Backend

* FastAPI (Python)

Database

* PostgreSQL
* pgvector for vector similarity search

AI Components

* Embeddings for semantic search
* Retrieval Augmented Generation (RAG)
* Language model API for explanations

---

# Project Architecture

RepoSage consists of several core components.

The user interacts with a web interface built with Next.js. The frontend communicates with a FastAPI backend using HTTP requests.

The backend processes repository uploads, reads source files, performs searches, and interacts with AI services.

A PostgreSQL database stores repository data, code chunks, and embedding vectors. Vector similarity search is used to retrieve relevant code for a given query.

The system then provides the retrieved code context to a language model to generate explanations.

More detailed design information is available in the documentation inside the `docs` folder.

---

# Project Status

RepoSage is currently under active development.

Development is organized into the following stages:

Sprint 0
Project setup and development environment.

Sprint 1
Frontend and backend communication.

Sprint 2
Repository upload and file exploration.

Sprint 3
Keyword search across repository files.

Sprint 4
Semantic search using embeddings.

Sprint 5
AI question answering using a RAG pipeline.

Sprint 6
Evaluation and system metrics.

Sprint 7
Deployment to cloud infrastructure.

---

# Running the Project

Frontend

Navigate to the frontend directory.

```
cd frontend
```

Install dependencies.

```
npm install
```

Start the development server.

```
npm run dev
```

The frontend will run locally at:

```
http://localhost:3000
```

Backend

Navigate to the backend directory.

```
cd backend
```

Run the FastAPI server.

```
uv run uvicorn app.main:app --reload
```

The backend server will run locally at:

```
http://localhost:8000
```

You can verify the server is running by visiting:

```
http://localhost:8000/health
```

---

# Documentation

Additional documentation can be found in the `docs` directory.

Current documentation includes:

* Architecture overview
* API specification

More documentation will be added as development continues.

---

# Future Improvements

Possible future improvements include:

* User authentication
* Repository history tracking
* Query history
* Improved code chunking strategies
* Streaming AI responses
* Advanced evaluation dashboards

---

# License

This project is currently developed for learning and portfolio purposes.
