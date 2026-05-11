# ADR-001: Stack сонголт

**Огноо:** 2025-04-28  
**Статус:** Accepted  
**Шийдвэр гаргагч:** Хөслэн + Claude

---

## Нөхцөл байдал

Personal Task Tracker REST API хөгжүүлэхийн тулд backend framework, database, тестийн хэрэгслийг сонгох шаардлагатай болсон. 2 долоо хоногийн хугацаанд ганцаараа хийх учраас setup complexity бага, AI code generation найдвартай, OpenAPI documentation автомат гарах stack хэрэгтэй байсан.

---

## Авч үзсэн сонголтууд

| | Stack A | Stack B | Stack C |
|--|---------|---------|---------|
| Backend | Node.js + Express | Python + FastAPI | Node.js + Fastify |
| Database | SQLite | MongoDB | PostgreSQL |
| Frontend | Vanilla JS | Vanilla JS | React |

---

## Шийдвэр

**Python + FastAPI + MongoDB + Vanilla JS** сонгосон.

---

## Үндэслэл

**FastAPI** сонгосон шалтгаан:
- OpenAPI spec автоматаар үүсгэдэг — assignment шаардлага хангана
- Pydantic validation автомат — код цэвэр байна
- Async/await native дэмжлэг — MongoDB Motor-тэй төгс нийцтэй
- AI-аас үүсгэсэн код найдвартай, жишээ олон

**MongoDB** сонгосон шалтгаан:
- Schema-less — task-ийн бүтэц өөрчлөгдөхөд flexible
- Labels массив хадгалахад зохистой
- Motor async driver FastAPI-тэй нийцтэй
- Docker-оор хурдан ажиллуулах боломжтой

**Vanilla JS** сонгосон шалтгаан:
- Build process шаардахгүй
- Assignment-ийн гол зорилго backend учраас frontend-д complexity нэмэхгүй байхаар шийдсэн

---

## Үр дагавар

- Python 3.12+ шаардагдана
- MongoDB 7.0+ (local эсвэл Docker) шаардагдана
- `motor`, `fastapi`, `pydantic`, `uvicorn` dependency болно
- Unit test-д `pytest`, `pytest-asyncio` ашиглана

