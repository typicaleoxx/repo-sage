# RepoSage API Specification

## Overview

The RepoSage backend exposes a set of REST API endpoints used by the frontend application.

The API is built using **FastAPI** and communicates using **JSON over HTTP**.

These endpoints allow the frontend to:

* verify server health
* upload repositories
* browse repository files
* search code
* perform semantic search
* ask questions about the repository

Base URL during development:

```
http://localhost:8000
```

---

# Health Endpoint

## GET /health

Returns a simple response confirming that the backend server is running.

### Request

No parameters required.

### Example Request

```
GET /health
```

### Example Response

```json
{
  "status": "ok"
}
```

### Purpose

This endpoint is used to verify that the backend service is operational.

It is typically used by:

* frontend startup checks
* monitoring tools
* deployment health checks

---

# Upload Repository

## POST /upload-zip

Uploads a repository ZIP file to the server.

The backend extracts the ZIP file, processes source files, and stores metadata about the repository.

### Request

Content-Type:

```
multipart/form-data
```

Field:

```
file: repository.zip
```

### Example Request

```
POST /upload-zip
```

Body:

```
file = my-repository.zip
```

### Example Response

```json
{
  "repo_id": "abc123",
  "file_count": 142
}
```

### Response Fields

| Field      | Description                                   |
| ---------- | --------------------------------------------- |
| repo_id    | Unique identifier for the uploaded repository |
| file_count | Number of supported files processed           |

---

# List Repository Files

## GET /repos/{repo_id}/files

Returns a list of all supported files inside a repository.

### Example Request

```
GET /repos/abc123/files
```

### Example Response

```json
[
  "src/auth/login.js",
  "src/auth/register.js",
  "src/database/connection.py",
  "README.md"
]
```

### Purpose

This endpoint allows the frontend to build a **file tree view** for repository exploration.

---

# Get File Content

## GET /repos/{repo_id}/files/content

Returns the contents of a specific file.

### Query Parameters

| Parameter | Description                 |
| --------- | --------------------------- |
| path      | File path inside repository |

### Example Request

```
GET /repos/abc123/files/content?path=src/auth/login.js
```

### Example Response

```json
{
  "path": "src/auth/login.js",
  "content": "function loginUser(username, password) { ... }"
}
```

---

# Keyword Search

## GET /repos/{repo_id}/search

Searches repository files using keyword matching.

### Query Parameters

| Parameter | Description  |
| --------- | ------------ |
| q         | search query |

### Example Request

```
GET /repos/abc123/search?q=login
```

### Example Response

```json
[
  {
    "file_path": "src/auth/login.js",
    "line_number": 42,
    "snippet": "function loginUser(username, password)"
  },
  {
    "file_path": "src/routes/auth.ts",
    "line_number": 10,
    "snippet": "router.post('/login', authenticateUser)"
  }
]
```

### Response Fields

| Field       | Description                       |
| ----------- | --------------------------------- |
| file_path   | File containing the match         |
| line_number | Line number of the match          |
| snippet     | Code snippet containing the match |

---

# Semantic Search

## POST /repos/{repo_id}/semantic-search

Performs semantic search using vector embeddings.

The query is converted into an embedding and compared with stored code chunk embeddings.

### Request

```json
{
  "query": "Where is authentication implemented?"
}
```

### Example Response

```json
[
  {
    "file_path": "src/auth/login.js",
    "start_line": 1,
    "end_line": 80,
    "content": "function loginUser(...) { ... }",
    "score": 0.89
  }
]
```

### Response Fields

| Field      | Description              |
| ---------- | ------------------------ |
| file_path  | File containing the code |
| start_line | Start line of code chunk |
| end_line   | End line of code chunk   |
| content    | Code snippet             |
| score      | Vector similarity score  |

---

# Ask Repository Question

## POST /repos/{repo_id}/ask

Allows users to ask natural language questions about the repository.

The backend executes a Retrieval Augmented Generation (RAG) pipeline to generate answers grounded in the repository code.

### Request

```json
{
  "question": "Where is authentication implemented?"
}
```

### Example Response

```json
{
  "answer": "Authentication is implemented in src/auth/login.js. The loginUser function validates credentials and creates a session token.",
  "references": [
    {
      "file": "src/auth/login.js",
      "lines": "1-80"
    }
  ]
}
```

### Response Fields

| Field      | Description                                |
| ---------- | ------------------------------------------ |
| answer     | AI generated explanation                   |
| references | Code locations used to generate the answer |

---

# Error Responses

All endpoints may return error responses.

Example:

```json
{
  "error": "Repository not found"
}
```

Typical error status codes:

| Code | Meaning               |
| ---- | --------------------- |
| 400  | Bad request           |
| 404  | Resource not found    |
| 500  | Internal server error |

---

# Future API Improvements

Future enhancements may include:

* authentication endpoints
* repository management APIs
* query history endpoints
* evaluation metrics endpoints
* streaming AI responses

These improvements would expand RepoSage into a production-grade developer tool.
