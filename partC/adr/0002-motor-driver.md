# ADR-002: Async Motor Driver сонгох шийдвэр

**Огноо:** 2025-05-10  
**Статус:** Accepted  
**Шийдвэр гаргагч:** Хөслэн + Claude

---

## Нөхцөл байдал

FastAPI нь async/await дэмждэг framework учраас MongoDB-тэй холбогдохдоо sync эсвэл async driver сонгох шийдвэр гарах шаардлагатай болсон.

Сонголтууд:
1. **PyMongo** — MongoDB-ийн албан ёсны sync Python driver
2. **Motor** — MongoDB-ийн async Python driver (PyMongo дээр суурилсан)
3. **Beanie** — Motor дээр суурилсан ODM (Object Document Mapper)

---

## Авч үзсэн сонголтууд

### PyMongo (sync)
- Давуу тал: сайн документтэй, тогтвортой, олон жишээтэй
- Сул тал: FastAPI-ийн async event loop-тэй зөрчилдөх, `run_in_executor` шаардагдах, performance муу

### Motor (async)
- Давуу тал: FastAPI-тэй төгс нийцтэй, async/await шууд дэмждэг, PyMongo-тэй ижил API
- Сул тал: PyMongo-оос арай цөөн жишээ байдаг

### Beanie (ODM)
- Давуу тал: Model-д суурилсан, validation автомат
- Сул тал: Нэмэлт abstraction layer, энгийн CRUD-д хэт их complexity

---

## Шийдвэр

**Motor** сонгосон.

---

## Үндэслэл

FastAPI нь async framework учраас sync driver (PyMongo) ашиглах нь event loop-г blocking хийж performance-д сөргөөр нөлөөлнө. Motor нь PyMongo-тэй ижил API-тай учраас суралцах curve бага. Beanie нь энэ хэмжээний төсөлд хэт их complexity нэмдэг.

AI-тай хийсэн ярилцлагад Motor-ийн `.find_one_and_update()` болон cursor-ийн `.to_list(length=...)` API-г хэрхэн зөв ашиглах талаар тодруулсан. Анхны AI санал `.to_list()` параметргүй ашиглаж байсан бол documentation шалгаж `length` parameter заавал шаардлагатайг тогтоосон.

---

## Үр дагавар

- Бүх database operation `async/await` ашиглана
- `motor.motor_asyncio.AsyncIOMotorClient` ашиглана
- Test-үүдэд `AsyncMock` ашиглан Motor-г mock хийнэ

