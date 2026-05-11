# Personal Task Tracker — Architecture

## System Overview

Python + FastAPI + MongoDB ашигласан REST API backend.

## Architecture Diagram

```mermaid
graph TD
    Client["Client (HTTP / Browser)"]
    API["FastAPI Application\n(main.py)"]
    Router["Task Router\n(routes/tasks.py)"]
    Service["Task Service\n(services.py)"]
    Models["Pydantic Models\n(models.py)"]
    DB["MongoDB\n(Motor async driver)"]
    DBConn["Database Connection\n(database.py)"]

    Client -->|HTTP Request| API
    API -->|Route| Router
    Router -->|Call| Service
    Service -->|Validate| Models
    Service -->|Query| DBConn
    DBConn -->|Async| DB
    DB -->|Result| DBConn
    DBConn -->|Return| Service
    Service -->|Serialize| Models
    Models -->|Response| Router
    Router -->|JSON| Client
```

## Module Description

| Module | Файл | Үүрэг |
|--------|------|-------|
| App Entry | `main.py` | FastAPI instance, CORS, lifespan, router бүртгэл |
| Database | `database.py` | Motor async client, connect/close |
| Models | `models.py` | Pydantic schema — TaskCreate, TaskUpdate, TaskResponse |
| Service | `services.py` | CRUD бизнес логик, MongoDB query |
| Router | `routes/tasks.py` | HTTP endpoint-ууд, query parameter |

## Data Flow

```mermaid
sequenceDiagram
    participant C as Client
    participant R as Router
    participant S as Service
    participant M as MongoDB

    C->>R: POST /api/tasks/ {title, priority, labels}
    R->>S: create_task(data)
    S->>S: validate + add timestamps
    S->>M: insert_one(doc)
    M-->>S: inserted_id
    S-->>R: TaskResponse
    R-->>C: 201 Created {id, title, ...}
```

## Layer Architecture

```
┌─────────────────────────────┐
│        HTTP Layer           │  FastAPI routes, request/response
├─────────────────────────────┤
│       Business Layer        │  services.py — CRUD logic
├─────────────────────────────┤
│        Data Layer           │  database.py + Motor driver
├─────────────────────────────┤
│         MongoDB             │  tasktracker database
└─────────────────────────────┘
```

## API Endpoints

| Method | Path | Тайлбар |
|--------|------|---------|
| POST | `/api/tasks/` | Task үүсгэх |
| GET | `/api/tasks/` | Жагсаалт + filter/search |
| GET | `/api/tasks/{id}` | Нэг task |
| PATCH | `/api/tasks/{id}` | Засах |
| DELETE | `/api/tasks/{id}` | Устгах |
| GET | `/api/tasks/labels` | Label жагсаалт |
| GET | `/health` | Health check |
