# Personal Task Tracker төслийн Stack Comparison

## Зорилго

Хэрэгжилт эхлэхээс өмнө энэхүү бие даалтын ажлыг ганцаарчлан, 2 долоо хоногийн хугацаанд хамгийн үр дүнтэй гүйцэтгэх боломжтой технологийн stack-ийг сонгохын тулд AI тусламжтайгаар 3 өөр хувилбарыг харьцуулан судлав.

Харьцуулалтыг дараах шалгуураар хийсэн:

- AI code generation хэр найдвартай байх
- Unit testing хийхэд хялбар эсэх
- Deployment болон ажиллуулахад төвөг багатай эсэх
- Цаашид maintain хийхэд ойлгомжтой эсэх

---

## Харьцуулсан боломжит stack-ууд

### Stack A
Node.js + Express + MongoDB + Vanilla JavaScript

### Stack B
Python + FastAPI + SQLite + Vanilla JavaScript

### Stack C
Node.js + Fastify + PostgreSQL + React

---

## Харьцуулалтын хүснэгт

| Шалгуур | Stack A: Express | Stack B: FastAPI | Stack C: Fastify + React |
|---------|------------------|------------------|---------------------------|
| Setup Complexity | Маш бага | Бага | Өндөр |
| Суралцах төвшин | Хялбар | Хялбар–дунд | Дунд–өндөр |
| AI Code Generation Quality | Маш сайн | Маш сайн | Сайн |
| OpenAPI Documentation | Гараар нэмэлтээр | Автоматаар үүснэ | Гараар тохируулна |
| Testing хийхэд | Jest / Supertest | pytest / TestClient | Илүү төвөгтэй |
| Database Setup | Маш хялбар | Маш хялбар | PostgreSQL server шаардлагатай |
| Frontend Complexity | Маш бага | Маш бага | React build шаардлагатай |
| Deployment Ease | Хялбар | Хялбар | Дунд |
| Maintainability | Сайн | Маш сайн | Сайн боловч илүү complex |

---

## Stack тус бүрийн дүн шинжилгээ

### Stack A — Node.js + Express + SQLite + Vanilla JS

Энэхүү stack нь backend хөгжүүлэлтийн хамгийн түгээмэл beginner хувилбаруудын нэг юм.  
Express framework-ийн жишээ код, documentation маш их байдаг тул AI-аас код үүсгүүлэхэд найдвартай. SQLite ашигласнаар тусдаа database server ажиллуулах шаардлагагүй.

Гэвч энэ stack-ийн сул тал нь OpenAPI specification автоматаар үүсгэдэггүй тул assignment-ийн `openapi.yaml` шаардлагыг биелүүлэхийн тулд нэмэлт гар ажиллагаа шаардагдана.

---

### Stack B — Python + FastAPI + SQLite + Vanilla JS

FastAPI нь орчин үеийн REST API framework бөгөөд:

- request validation автоматаар хийдэг,
- API documentation автоматаар гаргадаг,
- route бүтэц нь ойлгомжтой,
- Pydantic schema ашигладаг тул өгөгдлийн бүтэц тодорхой байдаг.

Мөн `/openapi.json` файлыг автоматаар үүсгэдэг нь Part B-ийн `openapi.yaml` гаргах ажлыг маш их хөнгөвчилнө.

Unit test бичихэд `pytest` болон `TestClient` ашиглахад энгийн бөгөөд AI generated test code-ийг шалгаж засварлахад ойлгомжтой.

---

### Stack C — Node.js + Fastify + PostgreSQL + React

Энэ stack нь production түвшний системд илүү тохиромжтой боловч энэхүү 2 долоо хоногийн solo assignment-д шаардлагагүйгээр complexity нэмнэ.

- PostgreSQL тусдаа server тохируулах шаардлагатай
- React frontend build process орно
- Fastify ecosystem Express-ээс бага

Иймээс хөгжүүлэлтийн хурд удаашрах эрсдэлтэй.

---

## Эцсийн сонголт

**Сонгосон stack: Python + FastAPI + SQLite + Vanilla JavaScript**

Энэхүү stack-ийг сонгосон үндсэн шалтгаанууд:

- Setup хийхэд харьцангуй энгийн
- AI-аар код үүсгүүлэхэд тогтвортой
- OpenAPI documentation автоматаар гарна
- Unit testing хийхэд хялбар
- Кодын бүтэц цэвэр, maintain хийхэд ойлгомжтой

Ялангуяа assignment-ийн шаардлагад байгаа `openapi.yaml` файлыг хамгийн бага нэмэлт ажиллагаатай гаргах боломжтой нь хамгийн том давуу тал болсон.

---

## Дүгнэлт

AI-assisted planning ашиглан 3 өөр stack-ийг харьцуулсны үр дүнд Python + FastAPI + SQLite + Vanilla JavaScript нь энэхүү бие даалтын ажилд хамгийн оновчтой сонголт гэж үзэв.

Энэ нь шаардлагагүй framework complexity-ийг багасгаж, богино хугацаанд чанартай REST API болон minimal frontend бүтээх боломжийг олгоно.
