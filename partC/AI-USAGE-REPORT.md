# AI Usage Report — F.CSM311 Бие даалт 13

**Огноо:** 2025-05-10  
**Төсөл:** Personal Task Tracker API (Python + FastAPI + MongoDB)  
**Ашигласан AI хэрэгсэл:** Claude (Anthropic)

---

## 1. Юуг AI хийсэн, юуг өөрөө хийсэн?

### AI хийсэн зүйлс

**Part A — Plan:**
- Stack харьцуулалтын хүснэгт (FastAPI vs Flask vs Express) үүсгэхэд AI-г ашигласан. Гурван stack-ийн давуу болон сул талуудыг жагсааж, MongoDB-тэй хамгийн сайн нийцэх stack-ийг тодорхойлоход тусалсан.
- ARCHITECTURE.md дэх Mermaid diagram-ын бүтцийг AI санал болгосон. Module хоорондын холболт, data flow-г зөв дүрслэхэд хамтран ажилласан.
- CLAUDE.md-ийн no-go zones болон convention хэсгийг AI draft хийсэн.
- ADR-001 stack decision-ы үндэслэлийн хэсгийг AI тусалж бичсэн.

**Part B — Build:**
- `models.py` дэх Pydantic schema-г AI үүсгэсэн. TaskCreate, TaskUpdate, TaskResponse гэсэн гурван model-ийг зөв зохион байгуулсан.
- `services.py` дэх CRUD функцуудын бүтцийг AI санал болгосон. Ялангуяа `_serialize()` helper функц болон MongoDB ObjectId validation-г хэрхэн зохион байгуулах талаар AI тусалсан.
- `routes/tasks.py` дэх endpoint-уудын Query parameter тодорхойлолтыг AI бичсэн.
- `test_tasks.py` дэх 16 unit test-ийн ерөнхий бүтэц болон mock strategy-г AI санал болгосон.
- `openapi.yaml` spec-ийн бүтцийг AI үүсгэсэн.

### Өөрөө хийсэн зүйлс

- **Stack сонголт:** FastAPI + MongoDB-г сонгох шийдвэрийг өөрөө гаргасан. Async support болон MongoDB-тэй Motor driver-ийн нийцтэй байдал чухал байсан учраас энэ сонголт хийсэн.
- **Төслийн бүтэц:** `src/`, `tests/`, `routes/` гэсэн фолдер бүтцийг өөрөө тогтоосон.
- **AI гаргасан кодын review:** AI үүсгэсэн код бүрийг уншиж, логикийг ойлгож, шаардлагатай газар засварласан. Ялангуяа `services.py` дэх filter logic-г өөрчилсөн.
- **Git workflow:** Commit message бичих, өдөр бүр тодорхой хэсгийг commit хийх ажлыг өөрөө удирдсан.
- **Тест ажиллуулах, debug хийх:** `pytest` ажиллуулж, алдааг олж засах ажлыг өөрөө хийсэн.

---

## 2. Hallucination — AI ямар буруу зүйл санал болгосон?

### Жишээ 1: Motor driver-ийн буруу API

AI анх `services.py`-д MongoDB cursor ашиглахдаа дараах код санал болгосон:

```python
# AI санал болгосон (буруу)
tasks = await db.tasks.find(query).to_list()
```

Гэвч Motor 3.x хувилбарт `.to_list()` заавал `length` parameter шаарддаг:

```python
# Зөв код
tasks = await db.tasks.find(query).skip(skip).limit(limit).to_list(length=limit)
```

Энэ алдааг `uvicorn` ажиллуулахад `TypeError` гарч ирснээр олж мэдсэн. Motor-ийн official documentation-г шалгаж зөв хувилбарыг олсон.

### Жишээ 2: Pydantic v2-ийн deprecated method

AI `models.py`-д Pydantic v1-ийн syntax ашигласан:

```python
# AI санал болгосон (Pydantic v1 — буруу)
doc = data.dict()
```

Pydantic v2-т `.dict()` нь deprecated болж `.model_dump()` болсон байдаг:

```python
# Pydantic v2-д зөв
doc = data.model_dump()
```

Энэ алдааг `DeprecationWarning` харж мэдсэн. Pydantic v2 migration guide-г уншиж бүх `.dict()` дуудлагыг `.model_dump()` болгон зассан.

---

## 3. Security болон License-ийн анхаарал

### Security жишээ: MongoDB Injection эрсдэл

AI анх search functionality-г дараах байдлаар санал болгосон:

```python
# AI анхны санал (эрсдэлтэй)
query["title"] = search  # шууд string оруулах
```

Энэ нь MongoDB query injection-д өртөмтгий байсан. Хэрэглэгч `{"$gt": ""}` гэх мэт MongoDB operator оруулвал бүх document-уудыг буцааж болох байсан.

Зөв хувилбарт regex-тэй `$options: "i"` ашиглан input-г string болгон хязгаарласан:

```python
# Засварласан (аюулгүй)
query["$or"] = [
    {"title": {"$regex": search, "$options": "i"}},
    {"description": {"$regex": search, "$options": "i"}},
]
```

Мөн OWASP Top 10-д NoSQL Injection (A03: Injection) орсон байдаг тул `/review` slash command ашиглан кодоо шалгасан.

---

## 4. Юуг AI-аар хурдан хийсэн?

**Boilerplate код үүсгэх** хамгийн их цаг хэмнэсэн хэсэг байсан. FastAPI-д CRUD endpoint бүрийн бүтэц, Pydantic model-ийн тодорхойлолт, OpenAPI spec бичих ажлыг AI маш хурдан хийсэн. Өөрөө хийсэн бол энэ хэсэгт 3-4 цаг зарцуулах байсан ч AI-тай хамтран 30-40 минутад дуусгасан.

**Unit test бичих** мөн хурдан байсан. Mock strategy, fixture тохируулах, edge case олох ажлыг AI санал болгосон. 16 тест бичихэд бие даан хийсэн бол 2+ цаг шаардагдах байсан.

**OpenAPI spec үүсгэх** — endpoint бүрийн parameter, response schema бичих ажлыг AI хийсэн. Гараар бичсэн бол маш уйтгартай, алдаа гарах магадлал өндөр ажил байсан.

---

## 5. Юуг AI-аар удаан хийсэн?

**Hallucination засах** хамгийн их цаг зарцуулсан хэсэг байсан. AI буруу API санал болгоход зөв хувилбарыг олохын тулд documentation уншиж, туршиж үзэх шаардлагатай болсон. Заримдаа AI-г "засуулах" гэж дахин дахин асуухад цаг алдсан — шууд documentation уншсан нь хурдан байсан болов уу.

**Context алдах асуудал** — урт session-д AI өмнөх шийдвэрүүдийг мартаж, зөрчилтэй санал болгох тохиолдол гарсан. Жишээлбэл, `services.py`-д нэг gas pattern ашигласны дараа `routes/tasks.py`-д өөр pattern санал болгосон. Энэ тохиолдолд CLAUDE.md-г дахин уншуулж context-г сэргээх шаардлагатай болсон.

**Хэт их тайлбар** — заримдаа AI маш урт тайлбар бичиж, гол код нь алга болдог байсан. Товч, шууд хариулт авахын тулд prompt-оо нарийвчлан бичих хэрэгтэй болсон.

---

## 6. Skill Atrophy эрсдэлийг яаж зохицуулсан?

Энэ бие даалтыг хийх явцад "AI байхгүй бол би энэ кодыг бичиж чадах уу?" гэсэн асуулт байнга тавьж байсан.

**Хийсэн арга хэмжээнүүд:**

Нэгдүгээрт, AI үүсгэсэн код бүрийг мөр бүрээр нь уншиж, яагаад ийм бичсэнийг ойлгохыг хичээсэн. Зүгээр copy-paste хийгээгүй.

Хоёрдугаарт, `services.py`-ийн зарим функцийг эхлээд өөрөө бичиж үзээд, AI-н хувилбартай харьцуулсан. Ингэж өөрийн ойлголт болон AI-н санал хоёрын зөрүүг харсан.

Гуравдугаарт, unit test-үүдийг AI бичсэн ч тест бүрийг ажиллуулж, яагаад pass болсон, fail болсон шалтгааныг ойлгосон.

Дөрөвдүгээрт, багш "шалгалт AI байхгүй явагдана" гэж хэлсэн учраас FastAPI-ийн үндсэн concept-үүдийг — dependency injection, lifespan, async/await — дахин давтан судалсан.

Skill atrophy-г бүрэн зайлсхийж чадсан гэж хэлэхэд хэцүү. Гэхдээ AI-г "бичүүлэх" хэрэгсэл биш "хурдасгах" хэрэгсэл болгон ашигласан нь чухал ялгаа байсан гэж боддог.

---

*Энэ report нь AI-тай хамтран ажилласан бодит туршлага дээр үндэслэсэн болно.*
