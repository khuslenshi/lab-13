# AI Session 03 — Testing Strategy

**Огноо:** 2026-05-11  
**Зорилго:** Unit test бичих strategy тогтоох, mock хэрхэн ашиглах

---

## Ярилцлагын товч

**Хэрэглэгч:** FastAPI + Motor-д unit test хэрхэн бичих вэ? Жинхэнэ MongoDB холбохгүйгээр.

**Claude:** `unittest.mock.AsyncMock` ашиглан Motor-г mock хийх, `patch("services.get_db")` ашиглан database-г орлуулах strategy санал болголоо.

**Хэрэглэгч:** `pytest-asyncio` тохируулах хэрэгтэй юу?

**Claude:** `pytest.ini`-д `asyncio_mode = auto` тохируулахыг санал болголоо.

**Асуудал:** AI `@pytest.mark.asyncio` decorator бүрд нэмэхийг санал болгосон, гэвч `asyncio_mode = auto` тохируулбал decorator шаардлагагүй болдог.

---

## Үр дүн

- 16 unit test бичигдсэн
- `AsyncMock` mock strategy хэрэгжсэн
- `pytest.ini` asyncio_mode = auto тохируулсан
- Hallucination:불필요한 decorator арилгасан
