# AI Session 01 — Feature Core Implementation

**Огноо:** 2026-05-05  
**Зорилго:** FastAPI + MongoDB CRUD endpoint-уудын үндсэн бүтцийг тогтоох

---

## Ярилцлагын товч

**Хэрэглэгч:** FastAPI + MongoDB ашиглан task CRUD хийх. models, services, routes хэрхэн зохион байгуулах вэ?

**Claude:** Гурван давхаргад хуваахыг санал болголоо:
- `models.py` — Pydantic schema (TaskCreate, TaskUpdate, TaskResponse)
- `services.py` — бизнес логик, MongoDB query
- `routes/tasks.py` — HTTP endpoint

**Хэрэглэгч:** `services.py`-д MongoDB cursor-г хэрхэн ашиглах вэ?

**Claude:** Motor async driver-т `.to_list(length=limit)` ашиглана гэж санал болгосон.

**Асуудал гарсан:** AI анх `.to_list()` параметргүй санал болгосон — Motor 3.x-д `length` заавал шаардлагатай байдаг. Documentation шалгаж засварласан.

---

## Үр дүн

- `models.py` — 3 Pydantic model үүссэн
- `services.py` — 6 async функц үүссэн
- `routes/tasks.py` — 6 endpoint үүссэн
- Hallucination: `.to_list()` → `.to_list(length=limit)` засварласан

