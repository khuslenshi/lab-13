# lab-13
# Бие даалт 13 — AI-Assisted Software Construction

**F.CSM311 Программ хангамжийн бүтээлт**  
**Оюутан:** Хөслэн  
**Төсөл:** Personal Task Tracker API  
**Stack:** Python + FastAPI + MongoDB

---

## Төслийн танилцуулга

Personal Task Tracker нь хэрэглэгчийн өдөр тутмын task-уудыг удирдах REST API систем юм. Task үүсгэх, засах, устгах, хайх, шүүх боломжтой.

## Repository Бүтэц

```
bie-daalt-13/
├── CLAUDE.md              # Build commands, conventions, no-go zones
├── .claude/commands/      # Custom slash commands
├── partA/                 # Plan — Architecture, Stack, ADR
├── partB/                 # Build — Source code, Tests, API spec
└── partC/                 # Reflect — AI Usage Report, Self Evaluation
```

## Хурдан эхлэх

```bash
# Dependencies
cd partB
pip install -r src/requirements.txt

# MongoDB ажиллуулах (Docker)
docker run -d -p 27017:27017 mongo:7

# Server
cd src
uvicorn main:app --reload
# → http://localhost:8000/docs
```

## Хэсгүүд

| Хэсэг | Агуулга |
|-------|---------|
| [Part A](./partA/) | Архитектур, Stack харьцуулалт, ADR-001 |
| [Part B](./partB/) | FastAPI src код, 16 unit test, OpenAPI spec |
| [Part C](./partC/) | AI Usage Report, Self Evaluation, ADR-002 |
