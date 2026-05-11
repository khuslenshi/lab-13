# AI Session 02 — Debug API Issues

**Огноо:** 2026-05-10  
**Зорилго:** Pydantic v2 migration болон Motor driver алдааг засах

---

## Ярилцлагын товч

**Хэрэглэгч:** `DeprecationWarning: The `dict` method is deprecated` гэсэн warning гарч байна.

**Claude:** Pydantic v2-т `.dict()` deprecated болсон, `.model_dump()` ашиглах хэрэгтэй гэж тайлбарлав.

**Хэрэглэгч:** `services.py`-д хаана байна вэ?

**Claude:** `data.dict()` → `data.model_dump()` болгон бүх газарт засахыг санал болголоо.

**Хэрэглэгч:** MongoDB search хийхэд injection эрсдэл байна уу?

**Claude:** Raw string query injection эрсдэлтэй, `$regex` + `$options: "i"` ашиглах нь аюулгүй гэж тайлбарлав.

---

## Үр дүн

- `.dict()` → `.model_dump()` бүгдэд засварласан
- Search query `$regex` ашиглан injection-с хамгаалсан
- Security: OWASP A03 Injection эрсдэл арилсан
