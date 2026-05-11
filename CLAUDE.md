
# CLAUDE.md — Personal Task Tracker

## Project Overview

Personal Task Tracker REST API — Python + FastAPI + MongoDB.  
F.CSM311 Бие даалт 13 — AI-Assisted Software Construction.

---

## Build & Run Commands

```bash
# Dependencies суулгах
cd partB
pip install -r src/requirements.txt

# Server ажиллуулах
cd partB/src
uvicorn main:app --reload

# Tests ажиллуулах
cd partB
python -m pytest tests/ -v
```

---

## Project Structure

```
partB/src/
├── main.py          # FastAPI app entry point
├── database.py      # MongoDB Motor connection
├── models.py        # Pydantic schemas
├── services.py      # Business logic / CRUD
└── routes/
    └── tasks.py     # API endpoints
```

---

## Code Conventions

- Python 3.12+
- Async/await — бүх database operation async байна
- Pydantic v2 — `.model_dump()` ашиглах (`.dict()` биш)
- Type hints — бүх функцэд заавал
- MongoDB ObjectId — `str` болгон serialize хийнэ
- Error handling — `HTTPException` ашиглана
- Timestamp — `datetime.now(timezone.utc)` ашиглана

---

## Naming Conventions

- File: `snake_case.py`
- Function: `snake_case`
- Class/Model: `PascalCase`
- Constant: `UPPER_SNAKE_CASE`
- Route: `/api/tasks/` (trailing slash)

---

## No-Go Zones

- `eval()`, `exec()` ашиглахгүй
- Raw string MongoDB query (injection эрсдэл) — regex `$options: "i"` ашиглана
- `.dict()` Pydantic v1 method ашиглахгүй — `.model_dump()` ашиглана
- Sync MongoDB call FastAPI дотор ашиглахгүй — заавал async Motor ашиглана
- `print()` debug-д ашиглахгүй — logger ашиглана
- Secret, API key-г code-д hardcode хийхгүй — `.env` ашиглана
- `.env` файлыг commit хийхгүй — зөвхөн `.env.example` commit хийнэ

---

## Git Conventions

- Conventional Commits format: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`
- AI ашигласан commit-д заавал: `Co-Authored-By: Claude <noreply@anthropic.com>`
- Feature нэг commit-д багтааж болохгүй — жижиг, тодорхой commit хийнэ

---

## Testing

- Framework: `pytest` + `pytest-asyncio`
- Mock: `unittest.mock.AsyncMock` MongoDB-г mock хийнэ
- Coverage: service layer бүрэн тестлэнэ
- Min: 10+ unit test pass болсон байна

---

## Custom Slash Commands

`.claude/commands/` дотор:
- `/review` — security + robustness шалгалт
- `/test` — edge case-тэй unit test үүсгэх
- `/docs` — JSDoc + README хэсэг
- `/commit` — Conventional Commits message
