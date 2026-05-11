# AI Session — Planning

**Огноо:** 2026-05-03  
**Зорилго:** Төслийн архитектур, stack сонголт, директор бүтэц тогтоох

---

## Ярилцлагын товч

**Хэрэглэгч:** Personal Task Tracker хийхэд ямар stack сонгох вэ? 3 сонголт харьцуул.

**Claude:** 3 stack харьцуулсан:
- Node.js + Express + SQLite
- Python + FastAPI + MongoDB  
- Node.js + Fastify + PostgreSQL + React

FastAPI-г санал болгосон шалтгаан: OpenAPI автомат, async native, Pydantic validation.

**Хэрэглэгч:** MongoDB-г яагаад SQLite-аас илүүд үзэх вэ?

**Claude:** Labels массив хадгалахад MongoDB flexible, Motor async driver FastAPI-тэй төгс нийцтэй гэж тайлбарлав.

**Хэрэглэгч:** Директор бүтэц яаж хийх вэ?

**Claude:** `src/`, `tests/`, `routes/` гэсэн давхарга санал болголоо.

---

## Үр дүн

- Stack: Python + FastAPI + MongoDB сонгосон
- Директор бүтэц тогтсон
- CLAUDE.md бичих төлөвлөгөө гарсан
- ADR-001 бичигдсэн

