# Báo Cáo Cá Nhân — Lab 7: Embedding & Vector Store

**Họ tên:** [Trần Thu Phương]
**Nhóm:** [G17]
**Ngày:** [19/9/2026]

> **Nộp 1 bản / sinh viên.** Phần nhóm (lựa chọn tài liệu, thiết kế chiến lược, bộ câu hỏi đánh giá, demo) nộp chung 1 bản trong `REPORT_NHOM.md`. Chi tiết thang điểm: `docs/SCORING.md`.

**Tổng điểm phần cá nhân: 60** = Khởi động (5) + Hướng tiếp cận (10) + Hoàn thiện code (30) + Dự đoán độ tương tự (5) + Kết quả truy xuất của tôi (10).

---

## 1. Khởi động (Warm-up) — Cá nhân (5 điểm)

### Độ tương tự Cosine (Cosine Similarity) (Bài tập 1.1)

**Độ tương tự cosine cao (High cosine similarity) nghĩa là gì?**
> Hai vector có hướng gần nhau trong không gian embedding, nên nội dung được mô hình biểu diễn là tương tự. Giá trị càng gần 1 thì mức tương đồng theo embedding càng cao; gần 0 là ít liên hệ và âm là ngược hướng.

**Ví dụ có độ tương tự CAO:**
- Câu A: `student financial aid`
- Câu B: `scholarship support for students`
- Tại sao tương đồng: Cùng nói về hỗ trợ tài chính cho sinh viên.

**Ví dụ có độ tương tự THẤP:**
- Câu A: `student financial aid`
- Câu B: `weather forecast tomorrow`
- Tại sao khác: Một câu nói về học bổng, câu kia nói về thời tiết.

**Tại sao độ tương tự cosine (cosine similarity) được ưu tiên hơn khoảng cách Euclid (Euclidean distance) cho text embeddings?**
> Cosine tập trung vào hướng của vector và ít bị ảnh hưởng bởi độ dài văn bản, phù hợp khi so sánh ngữ nghĩa của text embeddings. Khoảng cách Euclid dễ bị chi phối bởi độ lớn vector, dù hai văn bản có hướng biểu diễn tương tự.

### Bài toán tính toán Chunking (Bài tập 1.2)

**Tài liệu 10,000 ký tự, chunk_size=500, overlap=50. Bao nhiêu chunks?**
> Với chunk đầu tiên, bước dịch là `chunk_size - overlap = 500 - 50 = 450`. Số chunk là `ceil((10000 - 500) / 450) + 1 = 23`.
> **Đáp án:** 23 chunks.

**Nếu độ chồng chéo (overlap) tăng lên 100, số lượng chunk thay đổi thế nào? Tại sao muốn độ chồng chéo nhiều hơn?**
> Khi overlap tăng lên 100, bước dịch còn `500 - 100 = 400`, nên số chunk là `ceil(9500 / 400) + 1 = 25`. Overlap lớn giúp giữ ngữ cảnh ở ranh giới chunk nhưng làm tăng số chunk và phần nội dung trùng lặp.

---

## 2. Hướng tiếp cận của tôi (My Approach) — Cá nhân (10 điểm)

Giải thích cách tiếp cận của bạn khi lập trình (implement) các phần chính trong gói `src`.

### Các hàm chia nhỏ (Chunking Functions)

**`SentenceChunker.chunk`** — hướng tiếp cận:
> `SentenceChunker` dùng regex `(?<=[.!?])\s+`, tức là chỉ tách sau dấu chấm, chấm than hoặc dấu hỏi khi theo sau là khoảng trắng. Lookbehind giữ lại dấu câu trong chunk. Input rỗng hoặc chỉ có whitespace trả về danh sách rỗng; số câu tối đa mỗi chunk được chặn tối thiểu là 1.

**`RecursiveChunker.chunk` / `_split`** — hướng tiếp cận:
> `RecursiveChunker` thử các separator theo thứ tự `\n\n`, `\n`, `. `, khoảng trắng và cuối cùng là cắt theo ký tự. Nếu đoạn hiện tại không vượt `chunk_size`, đó là base case và được trả nguyên; nếu dài hơn, đoạn được tách tiếp bằng separator ưu tiên thấp hơn rồi ghép các mảnh nhỏ khi còn vừa kích thước.

### Lớp EmbeddingStore

**`add_documents` + `search`** — hướng tiếp cận:
> `add_documents` chuyển mỗi `Document` thành record gồm ID, content, metadata copy và embedding rồi nối vào danh sách in-memory. `search` kết hợp cosine similarity với mức giao nhau của token query-content, sắp xếp giảm dần theo hybrid score và trả tối đa `top_k`, không đưa vector embedding vào output.

**`search_with_filter` + `delete_document`** — hướng tiếp cận:
> `search_with_filter` lọc metadata trước rồi mới chạy cùng `_search_records`, vì lấy top-k trước có thể làm mất tài liệu hợp lệ. `delete_document` giữ lại các record có `metadata['doc_id']` khác ID cần xóa và trả `True` nếu kích thước store giảm.

### Tác tử KnowledgeBaseAgent

**`answer`** — hướng tiếp cận:
> `answer` truy xuất top-k chunk, đánh số từng chunk `[1]`, `[2]` và kèm nguồn từ metadata. Prompt yêu cầu chỉ dùng context, nói rõ khi không tìm thấy và trích dẫn số chunk; store rỗng được xử lý trước để không gọi LLM vô ích.

---

## 3. Hoàn thiện code (Core Implementation) — Cá nhân (30 điểm)

Vượt qua bộ kiểm thử là điều kiện tính điểm phần này.

### Kết Quả Kiểm Thử (Test Results)

```
python -m pytest tests/ -v
============================= 42 passed in 0.11s ==============================
```

**Số lượng bài test vượt qua (pass):** 42 / 42

---

## 4. Dự đoán độ tương tự (Similarity Predictions) — Cá nhân (5 điểm)

| Cặp | Câu A | Câu B | Dự đoán | Điểm thực tế | Đúng? |
|------|-----------|-----------|---------|--------------|-------|
| 1 | `scholarship amount` | `scholarship amount` | cao | 1.000000 | Có |
| 2 | `student financial aid` | `student financial aid` | cao | 1.000000 | Có |
| 3 | `tuition fee waiver` | `weather forecast tomorrow` | thấp | 0.198013 | Có |
| 4 | `CMC scholarship eligibility` | `library opening hours` | thấp | 0.084458 | Có |
| 5 | `mathematics scholarship` | `weather forecast tomorrow` | thấp | 0.006003 | Có |

**Kết quả nào bất ngờ nhất? Điều này nói gì về cách embeddings biểu diễn ý nghĩa?**
> Các cặp giống hệt nhau đạt 1.0, còn các cặp khác chủ đề có điểm thấp. Kết quả này xác nhận hàm cosine hoạt động đúng về mặt hình học, nhưng `_mock_embed` vẫn chỉ phù hợp để kiểm thử giao diện, không phải để kết luận chất lượng ngữ nghĩa tiếng Việt.

---

## 5. Kết quả truy xuất của tôi (Competition Results) — Cá nhân (10 điểm)

Chạy **5 câu hỏi đánh giá của nhóm** trên mã nguồn cá nhân của bạn trong gói `src`. **5 câu hỏi này phải trùng với các thành viên cùng nhóm** (xem `REPORT_NHOM.md`).

| # | Câu hỏi (Query) | Top-1 Chunk truy xuất được (tóm tắt) | Điểm Score | Có liên quan không? (Relevant) | Câu trả lời của Agent (tóm tắt) |
|---|-------|--------------------------------|-------|-----------|------------------------|
| 1 | Học bổng Sigma Gold có mức bao nhiêu mỗi tháng? | `viasm-sigma-gold-scholarship#2`: nguyên tắc chung; gold ở top-2 `#3` | 0.5213 | Có trong top-3 | Context top-2 chứa đúng mức 15 triệu đồng/tháng |
| 2 | Học bổng CMC Khai Phóng yêu cầu chứng chỉ tiếng Anh IELTS từ bao nhiêu? | `cmcu-scholarship-policy#2`: học bổng CMC Khai Phóng | 0.7040 | Có | Top-1 chứa điều kiện IELTS 7.5 |
| 3 | Hồ sơ học bổng Sigma Gold cho sinh viên năm thứ nhất gồm những giấy tờ nào? | `viasm-sigma-gold-scholarship#5`: hồ sơ yêu cầu | 0.5061 | Có | Top-1 chứa học bạ và giấy chứng nhận giải |
| 4 | Những đối tượng nào được miễn 100% học phí tại Đại học Công nghiệp Hà Nội? | `haui-financial-aid-scholarships#0`: giới thiệu HAUI; gold ở top-2 `#2` | 0.5460 | Có trong top-3 | Top-2 chứa đúng section miễn giảm học phí |
| 5 | Học bổng dành cho sinh viên ngành Toán được cấp theo tháng ở mức nào? | `viasm-sigma-gold-scholarship#2`: nguyên tắc chung; gold ở top-2 `#3` | 0.6050 | Có trong top-3 | Filter `audience=student` được áp dụng trước search; top-2 chứa mức 15 triệu đồng/tháng |

**Bao nhiêu câu hỏi trả về chunk có liên quan trong top-3?** 5 / 5

**Điều hay nhất tôi học được từ thành viên khác / nhóm khác (qua demo):**
> HeadingChunker giữ được tiêu đề section trong từng chunk, nên khi truy xuất đúng thì người đọc biết ngay chunk thuộc mục quy định nào. Sau khi kết hợp lexical overlap với cosine score, cả 5/5 câu đều có gold chunk trong top-3; các câu 1, 4 và 5 có gold ở top-2 thay vì top-1.

---

## Tự Đánh Giá (Phần Cá Nhân)

| Tiêu chí | Điểm tự đánh giá |
|----------|-------------------|
| Khởi động (Warm-up) | 5 / 5 |
| Hướng tiếp cận của tôi (My Approach) | 10 / 10 |
| Hoàn thiện code (Core Implementation — tests) | 30 / 30 |
| Dự đoán độ tương tự (Similarity Predictions) | 5 / 5 |
| Kết quả truy xuất của tôi (Competition Results) | 10 / 10 |
| **Tổng tự đánh giá** | **60 / 60** |
