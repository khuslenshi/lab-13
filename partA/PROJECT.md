# Personal Task Tracker төслийн ерөнхий төлөвлөгөө

## 1. Төслийн товч танилцуулга

Энэхүү төслийн хүрээнд хэрэглэгчийн өдөр тутмын хийх ажлуудыг удирдах зориулалттай энгийн боловч ажиллагаатай Personal Task Tracker систем хөгжүүлнэ.  
Систем нь REST API backend болон minimal frontend бүтэцтэй байх бөгөөд хэрэглэгч өөрийн task-уудыг нэмэх, засах, устгах, хайх, ангилах боломжтой байна.

Энэхүү сэдвийг сонгосон шалтгаан нь:

- CRUD үйлдлүүдийг бүрэн харуулах боломжтой,
- database interaction шаарддаг,
- search/filter зэрэг нэмэлт feature оруулах боломжтой,
- AI-assisted software construction workflow хэрэгжүүлэхэд тохиромжтой жижиг хэмжээний систем юм.

---

## 2. Төслийн зорилго

Төслийн үндсэн зорилго нь AI тусламжтайгаар богино хугацаанд жижиг хэмжээний программ хангамжийг төлөвлөж, хэрэгжүүлж, тестлэж, эргэцүүлэн дүгнэх software construction workflow-г туршихад оршино.

Үүний хүрээнд:

- backend API design хийх,
- frontend-ээс API хэрэглэж өгөгдөл харуулах,
- SQLite database ашиглан task хадгалах,
- AI-аар код generation хийлгэж review хийх,
- AI session log болон architecture decision record хөтлөх

ажлуудыг гүйцэтгэнэ.

---

## 3. Зорилтот хэрэглэгч

Энэхүү системийн зорилтот хэрэглэгч нь:

- хувийн ажлаа тэмдэглэж хянах хүсэлтэй оюутан,
- өдөр тутмын жижиг төлөвлөгөөтэй хэрэглэгч,
- deadline бүхий task-уудаа удирдах шаардлагатай хүн байна.

Систем нь олон хэрэглэгчийн authentication хийхгүй бөгөөд single-user local productivity tool байдлаар хөгжүүлэгдэнэ.

---

## 4. Үндсэн feature-үүд

Төсөлд дараах 5 үндсэн feature хэрэгжинэ.

### Feature 1 — Task Create
Хэрэглэгч шинэ task үүсгэж:

- гарчиг,
- тайлбар,
- due date,
- priority,
- label

мэдээллийг хадгална.

### Feature 2 — Task List / Read
Өмнө хадгалсан бүх task-уудыг жагсаалт хэлбэрээр харах боломжтой.

### Feature 3 — Task Update
Байгаа task-ийн мэдээллийг засварлах боломжтой.

### Feature 4 — Task Delete
Шаардлагагүй task-ийг устгах боломжтой.

### Feature 5 — Search and Filter
Task-уудыг:

- priority,
- label,
- due date,
- keyword

зэргээр шүүх болон хайх боломжтой.

---

## 5. Хийхгүй зүйлс (Non-goals)

Энэхүү assignment-ийн хугацаа болон scope-ийг хэт тэлэхгүй байх үүднээс дараах зүйлсийг хийхгүй.

- user authentication
- cloud deployment
- notification system
- complex UI framework
- multi-user collaboration

---

## 6. Minimum Viable Scope

2 долоо хоногийн хугацаанд дараах хэмжээнд ажил бүрэн хийгдсэн байхыг minimum viable scope гэж тодорхойлов.

- REST API бүрэн ажиллах
- SQLite database холбогдсон байх
- minimal HTML/CSS/JavaScript frontend ажиллах
- 10+ unit test pass болох
- OpenAPI specification гарсан байх

---

## 7. Дүгнэлт

Personal Task Tracker нь хэмжээний хувьд хэт том биш боловч backend, database, testing, API documentation, AI collaboration зэрэг энэхүү бие даалтын бүх үндсэн шаардлагыг хангах боломжтой тул сонгон хэрэгжүүлэхэд тохиромжтой төсөл гэж үзэв.

