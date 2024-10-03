# Similarity Search System with Qdrant

A Python-based Similarity Search System using FastAPI and Qdrant.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)

## Introduction

This application allows users to input a query and receive the top 3 most similar sentences from a whitepaper, based on
vector embeddings and similarity search using Qdrant.

## Prerequisites

- Docker
- Docker Compose

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/similarity-search-qdrant.git
cd similarity-search-qdrant
```

### 2. Create `.env` file

```
   QDRANT_HOST=172.33.0.2
   QDRANT_PORT=6333
   QDRANT_DEFAULT_COLLECTION_NAME=test
   ```

### 3.Run `sh run.sh`

## Usage

Swagger docs are available at `http://localhost:8001/docs`

Test curl query  to check everything is working fine

```bash
curl -X POST "http://localhost:8001/api/v1/search" \
     -H "Content-Type: application/json" \
     -d '{"input_query": "What the AI maturity themes are?"}'
```

## Tests

Are located in `tests` folder. To run tests, execute the following command (Be sure to run the command from the internal venv):

```bash
pytest 