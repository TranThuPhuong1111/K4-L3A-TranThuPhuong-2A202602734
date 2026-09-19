# Báo Cáo Nhóm — Lab 7: Embedding & Vector Store

**Nhóm:** [G17]
**Thành viên:** [Trần Thu Phương]
**Ngày:** [19/9/2026]

> **Nộp 1 bản / nhóm.** Phần cá nhân (hướng tiếp cận, kết quả riêng, dự đoán…) mỗi thành viên nộp riêng trong `REPORT_CANHAN.md`. Chi tiết thang điểm: `docs/SCORING.md`.

**Tổng điểm phần nhóm: 40** = Lựa chọn tài liệu (10) + Thiết kế chiến lược (15) + Chất lượng truy xuất (10) + Thuyết trình (5).

---

## 1. Lựa chọn tài liệu (Document Set Quality) — Nhóm (10 điểm)

### Chủ đề (Domain) & Lý Do Chọn

**Chủ đề:** Học bổng và hỗ trợ tài chính cho sinh viên

**Tại sao nhóm chọn chủ đề này?**
> Nhóm chọn chủ đề này vì corpus có các quy định học bổng, mức hỗ trợ, điều kiện và hồ sơ từ các nguồn đại học công khai. Nội dung có cấu trúc theo mục rõ ràng, phù hợp để so sánh chunk theo heading với các chiến lược chia nhỏ tổng quát.

### Danh sách tài liệu (Data Inventory)

| # | Tên tài liệu | Nguồn (Source URL) | Ngày lấy / Phiên bản | Số ký tự | Metadata đã gán |
|---|--------------|------------|--------------------|----------|-----------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Danh sách kiểm tra quản trị dữ liệu (Data governance checklist):**
- [ ] Tập tài liệu (Corpus) chỉ chứa nguồn công khai/được phép dùng và không chứa dữ liệu cá nhân, thông tin đăng nhập hoặc tài liệu nội bộ.
- [ ] Mỗi tài liệu có `source_url`, `retrieved_at`, `document_version` (hoặc ngày hiệu lực) trong metadata.

### Cấu trúc Metadata (Metadata Schema)

| Trường metadata | Kiểu | Ví dụ giá trị | Tại sao hữu ích cho truy xuất (retrieval)? |
|----------------|------|---------------|-------------------------------|
| | | | |
| | | | |

---

## 2. Thiết kế chiến lược (Strategy Design) — Nhóm (15 điểm)

> Mỗi thành viên thử **một chiến lược khác nhau** trên cùng bộ tài liệu; nhóm tổng hợp và so sánh ở đây.

### Phân tích đường cơ sở (Baseline Analysis)

Chạy `ChunkingStrategyComparator().compare()` trên 2-3 tài liệu:

| Tài liệu | Chiến lược (Strategy) | Số lượng Chunk | Độ dài trung bình | Giữ được ngữ cảnh không? |
|-----------|----------|-------------|------------|-------------------|
| | FixedSizeChunker (`fixed_size`) | | | |
| | SentenceChunker (`by_sentences`) | | | |
| | RecursiveChunker (`recursive`) | | | |

Kết quả đo trên phần thân đã bỏ YAML frontmatter, `chunk_size=200`:

| Tài liệu | Chiến lược | Số lượng Chunk | Độ dài trung bình | Giữ được ngữ cảnh không? |
|---|---|---:|---:|---|
| `cmcu-scholarship-policy` | FixedSizeChunker | 33 | 197.09 | Thấp, có thể cắt giữa ý |
| `cmcu-scholarship-policy` | SentenceChunker | 5 | 978.40 | Tốt theo câu nhưng vượt xa ngưỡng |
| `cmcu-scholarship-policy` | RecursiveChunker | 34 | 141.56 | Khá, giữ được đoạn nhưng mất heading |
| `haui-financial-aid-scholarships` | FixedSizeChunker | 16 | 194.44 | Thấp, có thể cắt giữa ý |
| `haui-financial-aid-scholarships` | SentenceChunker | 5 | 469.80 | Tốt theo câu nhưng chunk dài |
| `haui-financial-aid-scholarships` | RecursiveChunker | 17 | 136.76 | Khá, giữ được đoạn nhưng mất heading |
| `huce-study-abroad-scholarships` | FixedSizeChunker | 5 | 178.40 | Chấp nhận được với tài liệu ngắn |
| `huce-study-abroad-scholarships` | SentenceChunker | 1 | 691.00 | Một chunk quá dài |
| `huce-study-abroad-scholarships` | RecursiveChunker | 4 | 171.25 | Khá |

### Chiến lược của từng thành viên

> Mỗi thành viên điền một khối dưới đây (copy thêm nếu nhóm có nhiều hơn 3 người).

**Thành viên 1 — [Tên]**
- **Loại chiến lược:** custom `HeadingChunker`
- **Mô tả & lý do chọn cho chủ đề này:** Tách trước mỗi heading Markdown để mỗi mục quy định trở thành một đơn vị ngữ nghĩa. Nếu mục quá dài, chunker dùng recursive splitting và gắn lại heading vào mọi mảnh con để không mất ngữ cảnh.
- **Code snippet (nếu custom):**
```python
# Dán mã nguồn (implementation) vào đây
```

**Thành viên 2 — [Tên]**
- **Loại chiến lược:**
- **Mô tả & lý do chọn:**
- **Code snippet (nếu custom):**

**Thành viên 3 — [Tên]**
- **Loại chiến lược:**
- **Mô tả & lý do chọn:**
- **Code snippet (nếu custom):**

### So Sánh Giữa Các Thành Viên

| Thành viên | Chiến lược (Strategy) | Điểm truy xuất (/10) | Điểm mạnh | Điểm yếu |
|-----------|----------|----------------------|-----------|----------|
| | | | | |
| | | | | |
| | | | | |

**Chiến lược nào tốt nhất cho chủ đề này? Tại sao?**
> *Viết 2-3 câu — đây là phần được đánh giá cao nhất (khả năng suy nghĩ & giải thích):*

---

## 3. Câu hỏi đánh giá & Chất lượng truy xuất (Retrieval Quality) — Nhóm (10 điểm)

### Câu hỏi đánh giá & Câu trả lời chuẩn (nhóm thống nhất)

> **Đúng 5 câu hỏi**, đa dạng, có thể kiểm chứng; **ít nhất 1 câu** cần lọc metadata mới trả lời tốt. Đây là bộ câu hỏi chung cho mọi thành viên chạy.

| # | Câu hỏi (Query) | Câu trả lời chuẩn (Gold Answer) | Chunk nào chứa thông tin? |
|---|-------|-------------------------------|--------------------------|
| 1 | Học bổng Sigma Gold có mức bao nhiêu mỗi tháng? | 15 triệu đồng/tháng. | `viasm-sigma-gold-scholarship#3` |
| 2 | Học bổng CMC Khai Phóng yêu cầu chứng chỉ tiếng Anh IELTS từ bao nhiêu? | IELTS 7.5 trở lên hoặc tương đương. | `cmcu-scholarship-policy#2` |
| 3 | Hồ sơ học bổng Sigma Gold cho sinh viên năm thứ nhất gồm những giấy tờ nào? | Bản sao học bạ lớp 12 và bản sao giấy chứng nhận đạt giải nhất, nhì cấp tỉnh/thành phố trở lên ở cấp THPT; có thể kèm thành tích, chứng chỉ học thuật và bài luận theo tài liệu. | `viasm-sigma-gold-scholarship#5` |
| 4 | Những đối tượng nào được miễn 100% học phí tại Đại học Công nghiệp Hà Nội? | Người có công hoặc con của người có công; mồ côi cả cha và mẹ; dân tộc thiểu số thuộc hộ nghèo/cận nghèo; hoặc dân tộc thiểu số rất ít người ở vùng khó khăn/đặc biệt khó khăn. | `haui-financial-aid-scholarships#2` |
| 5 | Học bổng dành cho sinh viên ngành Toán được cấp theo tháng ở mức nào? | Học bổng Sigma Gold dành cho sinh viên đại học chính quy ngành Toán, mức 15 triệu đồng/tháng. | `viasm-sigma-gold-scholarship#3` (filter `audience=student`) |

### Tổng hợp chất lượng truy xuất của nhóm

> Cách chấm (theo `docs/SCORING.md`): **2 điểm/câu** — top-3 chứa chunk liên quan + agent trả lời đúng (2), có liên quan nhưng thiếu/không ở top-1 (1), không có trong top-3 (0).

| # | Câu hỏi | Chiến lược tốt nhất cho câu này | Có chunk liên quan trong top-3? | Ghi chú |
|---|---------|-------------------------------|-------------------------------|---------|
| 1 | Sigma Gold: mức học bổng | HeadingChunker | Có chunk liên quan trong top-3 | Gold ở top-2 sau hybrid scoring |
| 2 | CMC Khai Phóng: điều kiện IELTS | HeadingChunker | Có chunk liên quan trong top-3 | Gold ở top-1 |
| 3 | Hồ sơ Sigma Gold năm thứ nhất | HeadingChunker | Có chunk liên quan trong top-3 | Gold ở top-1 |
| 4 | Đối tượng miễn 100% học phí | HeadingChunker | Có chunk liên quan trong top-3 | Gold ở top-2 |
| 5 | Mức học bổng ngành Toán, có filter | HeadingChunker | Có chunk liên quan trong top-3 | Filter trước search, gold ở top-2 |

**Lọc bằng metadata có giúp ích không? Ở câu hỏi nào?**
> Câu 5 được chạy với `metadata_filter={"audience": "student"}` và filter được áp dụng trước khi xếp hạng. Tuy nhiên, cả 5 tài liệu hiện tại đều có `audience: "student"`, nên corpus chưa có hai nhóm audience khác nhau để chứng minh việc lọc làm thay đổi kết quả; cần bổ sung tài liệu có audience khác nếu muốn đo đúng tình huống này.

---

## 4. Thuyết trình (Demo) & Bài học nhóm — Nhóm (5 điểm)

**Những phân tích (insights) hay nhất nhóm sẽ trình bày:**
> *Liệt kê 2-3 ý:*

**Bài học rút ra khi so sánh trong nhóm:**
> *Viết 2-3 câu — cùng tài liệu nhưng chiến lược khác nhau dẫn tới khác biệt gì?*

**Nếu làm lại, nhóm sẽ thay đổi gì trong chiến lược dữ liệu (data strategy)?**
> *Viết 2-3 câu:*

---

## Tự Đánh Giá (Phần Nhóm)

| Tiêu chí | Điểm tự đánh giá |
|----------|-------------------|
| Lựa chọn tài liệu (Document Set Quality) | / 10 |
| Thiết kế chiến lược (Strategy Design) | / 15 |
| Chất lượng truy xuất (Retrieval Quality) | / 10 |
| Thuyết trình (Demo) | / 5 |
| **Tổng phần nhóm** | **/ 40** |
