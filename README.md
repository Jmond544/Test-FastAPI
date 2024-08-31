# First steps with FastAPI

## Installation

```bash
pip install fastapi
```

## Run the server

```bash
uvicorn main:app --reload
```

## Requests

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text":"orange", "is_done":1}' 'http://localhost:8000/items'
curl -X GET -H "Content-Type: application/json" 'http://localhost:8000/items/0'
curl -X DELETE -H "Content-Type: application/json" 'http://localhost:8000/items/1'
```