from pathlib import Path

base = Path(__file__).resolve().parent.parent
folder = base / "data" / "hoc-bong"

files = {
    "cmcu-scholarship-policy.md": """---
doc_id: \"cmcu-scholarship-policy\"
title: \"Chính sách học bổng - Đại học CMC\"
source_url: \"https://cmcu.edu.vn/chinh-sach-hoc-bong/\"
retrieved_at: \"2026-09-19\"
document_version: \"not-stated\"
audience: \"student\"
department: \"financial-aid\"
category: \"scholarships\"
language: \"vi\"
---

# Chính sách học bổng - Đại học CMC

Tập đoàn Công nghệ CMC dành quỹ học bổng, ưu đãi “CMC – Vì bạn xứng đáng” trị giá 96 tỷ đồng cho thí sinh có thành tích học tập xuất sắc nhập học năm 2026.

## 1. Chính sách học bổng

### 1) Học bổng CMC Khai Phóng: 100% học phí toàn khóa

- Số lượng: 55 suất
- Cơ sở Hà Nội: 40 suất
- Cơ sở TP.HCM: 15 suất
- Trị giá: 100% học phí toàn khóa, không bao gồm học phí chương trình tiếng Anh
- Điều kiện: thí sinh đạt ít nhất một trong các tiêu chí sau:
  - đoạt giải nhất, nhì, ba trong các kỳ thi học sinh giỏi và kỳ thi Khoa học kỹ thuật cấp quốc gia, quốc tế từ năm 2023–2026;
  - có môn đoạt giải phù hợp với ngành học đăng ký xét tuyển;
  - tổng điểm thi tốt nghiệp THPT theo tổ hợp môn đăng ký xét tuyển năm 2026 đạt từ 35,00/40,00 điểm trở lên, bao gồm điểm cộng và ưu tiên;
  - có chứng chỉ tiếng Anh IELTS 7.5 trở lên hoặc tương đương, hoặc TOPIK II cấp độ 4 (182–189) đối với ngành Ngôn ngữ Hàn Quốc, hoặc HSK 6 đối với ngành Ngôn ngữ Trung Quốc;
  - kết quả học tập HK1 lớp 12 hoặc cả năm lớp 12 có môn Toán đạt từ 8,00 điểm trở lên.

### 2) Học bổng CMC Sáng Tạo: 70% học phí toàn khóa

- Số lượng: 95 suất
- Cơ sở Hà Nội: 70 suất
- Cơ sở TP.HCM: 25 suất
- Trị giá: 70% học phí toàn khóa, không bao gồm học phí chương trình tiếng Anh
- Điều kiện:
  - đoạt giải nhất, nhì, ba các cuộc thi học sinh giỏi cấp tỉnh, thành phố trực thuộc trung ương từ năm 2023–2026;
  - môn đoạt giải nằm trong tổ hợp xét tuyển vào ngành tương ứng;
  - điểm thi đánh giá năng lực CMC-TEST đạt từ 63,00/80,00 trở lên;
  - kết quả học tập THPT HK1 lớp 12 hoặc cả năm lớp 12 có ít nhất 6 môn, trong đó có môn Toán, đạt trung bình từ 9,00 trở lên và không môn nào dưới 6,50;
  - tổng điểm thi tốt nghiệp THPT theo tổ hợp môn đăng ký xét tuyển năm 2026 đạt từ 34,00/40,00 điểm trở lên;
  - có chứng chỉ IELTS 7.0 hoặc tương đương, hoặc TOPIK II cấp độ 4 (174–181) cho ngành Ngôn ngữ Hàn Quốc, hoặc HSK 5 cho ngành Ngôn ngữ Trung Quốc;
  - kết quả học tập HK1 lớp 12 hoặc cả năm lớp 12 có môn Toán đạt từ 8,00 điểm trở lên.

### 3) Học bổng CMC Tiên Phong: 50% học phí toàn khóa

- Số lượng: 130 suất
- Cơ sở Hà Nội: 90 suất
- Cơ sở TP.HCM: 40 suất
- Trị giá: 50% học phí toàn khóa, không bao gồm học phí chương trình tiếng Anh
- Điều kiện:
  - điểm thi đánh giá năng lực CMC-TEST đạt từ 61,00/80,00 trở lên;
  - kết quả học tập THPT HK1 lớp 12 hoặc cả năm lớp 12 có ít nhất 6 môn, trong đó có môn Toán, đạt trung bình từ 8,50 trở lên và không môn nào dưới 6,50;
  - tổng điểm thi tốt nghiệp THPT theo tổ hợp môn đăng ký xét tuyển năm 2026 đạt từ 33,00/40,00 điểm trở lên;
  - chứng chỉ ngoại ngữ tiếng Anh IELTS 6.5 trở lên hoặc tương đương, hoặc TOPIK II cấp độ 4 (166–173) cho ngành Ngôn ngữ Hàn Quốc;
  - kết quả học tập HK1 lớp 12 hoặc cả năm lớp 12 có môn Toán đạt từ 8,00 điểm trở lên.

### 4) Học bổng CMC Kiến Tạo: 30% học phí toàn khóa

- Số lượng: 245 suất
- Cơ sở Hà Nội: 170 suất
- Cơ sở TP.HCM: 75 suất
- Trị giá: 30% học phí toàn khóa, không bao gồm học phí chương trình tiếng Anh
- Điều kiện:
  - điểm thi đánh giá năng lực CMC-TEST đạt từ 59,00/80,00 trở lên;
  - kết quả học tập THPT HK1 lớp 12 hoặc cả năm lớp 12 có ít nhất 6 môn, trong đó có môn Toán, đạt trung bình từ 8,00 trở lên và không môn nào dưới 6,50;
  - tổng điểm thi tốt nghiệp THPT theo tổ hợp môn đăng ký xét tuyển năm 2026 đạt từ 32,00/40,00 điểm trở lên;
  - chứng chỉ ngoại ngữ tiếng Anh IELTS 6.0 trở lên hoặc tương đương;
  - kết quả học tập HK1 lớp 12 hoặc cả năm lớp 12 có môn Toán đạt từ 8,00 điểm trở lên.

## 2. Chính sách ưu đãi

### Ưu đãi tặng iPad hoặc máy tính bảng

Thí sinh nhập học năm 2026 sẽ được tặng 01 chiếc iPad hoặc máy tính bảng tương đương nếu đặt CMC là nguyện vọng 1, 2, 3 và thỏa mãn ít nhất một trong các tiêu chí sau:

- tham dự kỳ thi Đánh giá năng lực năm 2026 của Trường Đại học CMC (CMC-TEST);
- tổng điểm kết quả học tập THPT HK1 lớp 12 hoặc cả năm lớp 12 theo tổ hợp môn đăng ký xét tuyển năm 2026 đạt từ 31,00/40,00 điểm trở lên;
- thí sinh là con đẻ, anh/chị/em ruột của nhân viên thuộc Tập đoàn Công nghệ CMC hoặc sinh viên đã tốt nghiệp/đang theo học tại Trường Đại học CMC.

### Ưu đãi cho con, anh/chị/em ruột của nhân viên CMC

- Trị giá ưu đãi: 20% học phí toàn khóa học
- Điều kiện: thí sinh nhập học năm 2026 thỏa mãn ít nhất một trong các tiêu chí sau:
  - là con đẻ, anh/chị/em ruột của nhân viên đang công tác tại các đơn vị thuộc Tập đoàn Công nghệ CMC, với thời gian công tác từ 3 năm trở lên tính tới ngày nhập học;
  - có anh/chị/em ruột đã tốt nghiệp hoặc đang học tập tại Trường Đại học CMC.

## 3. Chính sách hỗ trợ tài chính

Trường Đại học CMC hỗ trợ thí sinh hoàn thành thủ tục vay tín dụng theo quy định của Ngân hàng Chính sách xã hội và các ngân hàng khác.

## 4. Hồ sơ đăng ký xét học bổng

- Đăng ký xét tuyển học bổng tại: xettuyen.cmcu.edu.vn
- Bản PDF hoặc ảnh CCCD
- Giấy chứng nhận điểm thi THPT năm 2026 (bản photo có công chứng)
""",
    "haui-financial-aid-scholarships.md": """---
doc_id: \"haui-financial-aid-scholarships\"
title: \"Học bổng và hỗ trợ tài chính cho sinh viên - Đại học Công nghiệp Hà Nội\"
source_url: \"https://www.haui.edu.vn/vn/hoc-bong-hoc-phi/ho-tro-tai-chinh-va-hoc-bong-danh-cho-sinh-vien-haui/68191\"
retrieved_at: \"2026-09-19\"
document_version: \"not-stated\"
audience: \"student\"
department: \"financial-aid\"
category: \"scholarships\"
language: \"vi\"
---

# Học bổng và hỗ trợ tài chính cho sinh viên - Đại học Công nghiệp Hà Nội

Trong quá trình học tập tại Đại học Công nghiệp Hà Nội, sinh viên có thể tiếp cận nhiều chính sách hỗ trợ tài chính và học bổng, bao gồm miễn, giảm học phí, hỗ trợ học phí, hỗ trợ vay vốn, học bổng khuyến khích học tập và học bổng từ doanh nghiệp, tổ chức, đối tác.

## I. Hỗ trợ tài chính

### 1. Chính sách miễn giảm học phí

Căn cứ Nghị định số 238/2025/NĐ-CP ngày 03/09/2025 của Chính phủ về chính sách học phí, miễn, giảm, hỗ trợ học phí, hỗ trợ chi phí học tập và giá dịch vụ trong lĩnh vực giáo dục.

Đối tượng và mức hỗ trợ:

- Miễn 100% học phí:
  - sinh viên là người có công với cách mạng hoặc con đẻ/con nuôi của người có công với cách mạng;
  - sinh viên mồ côi cả cha và mẹ;
  - sinh viên là người dân tộc thiểu số thuộc hộ nghèo/cận nghèo;
  - sinh viên là người dân tộc thiểu số rất ít người ở vùng có điều kiện kinh tế - xã hội khó khăn hoặc đặc biệt khó khăn.

- Giảm 70% học phí:
  - sinh viên hệ Cao đẳng học một số ngành nghề nặng nhọc, độc hại, nguy hiểm;
  - sinh viên người dân tộc thiểu số có nơi thường trú tại thôn/bản đặc biệt khó khăn, xã khu vực III vùng đồng bào dân tộc thiểu số và miền núi, xã đặc biệt khó khăn vùng bãi ngang, ven biển và hải đảo.

- Giảm 50% học phí:
  - sinh viên có cha hoặc mẹ bị tai nạn lao động hoặc mắc bệnh nghề nghiệp được hưởng trợ cấp thường xuyên.

Mức miễn, giảm được tính theo học phí các học phần của lần học thứ nhất trong chương trình đào tạo chuẩn, không bao gồm các môn học kỹ năng sử dụng công nghệ thông tin, ngoại ngữ và các môn học khác theo yêu cầu của chương trình.

### 2. Chính sách hỗ trợ chi phí học tập

Căn cứ Quyết định số 66/2013/QĐ-TTg ngày 11/11/2013 của Chính phủ về chính sách hỗ trợ chi phí học tập đối với sinh viên dân tộc thiểu số học tại cơ sở giáo dục đại học.

- Mức hỗ trợ: 60% mức lương cơ sở
- Thời gian cấp: 10 tháng/năm
- Đối tượng: sinh viên hệ đại học chính quy là người dân tộc thiểu số có cha hoặc mẹ hoặc cả cha và mẹ hoặc ông bà (nếu sinh viên ở với ông bà) thuộc hộ nghèo hoặc hộ cận nghèo theo quy định của Nhà nước.

### 3. Chính sách hỗ trợ học tập

Bên cạnh các chính sách miễn, giảm học phí và hỗ trợ chi phí học tập, trường còn có các chương trình hỗ trợ học tập, học bổng khuyến khích và hỗ trợ vay vốn nhằm tạo điều kiện cho sinh viên hoàn thành tốt chương trình đào tạo.
""",
    "huce-study-abroad-scholarships.md": """---
doc_id: \"huce-study-abroad-scholarships\"
title: \"Học bổng du học - Đại học Xây dựng Hà Nội\"
source_url: \"https://tuyensinh.huce.edu.vn/hoc-bong-du-hoc\"
retrieved_at: \"2026-09-19\"
document_version: \"not-stated\"
audience: \"student\"
department: \"financial-aid\"
category: \"scholarships\"
language: \"vi\"
---

# Học bổng du học - Đại học Xây dựng Hà Nội

Trang tuyển sinh của Đại học Xây dựng Hà Nội hiển thị chủ đề “Học bổng du học” nhưng nội dung chi tiết chính thức không được thu thập đầy đủ trong trang này. Nội dung hiện có trong file chỉ ghi nhận tiêu đề và liên kết nguồn gốc, không có thông tin điều kiện, mức học bổng hay thời hạn cụ thể được lưu trữ trong bản crawl thu được.

## Ghi chú

- Nguồn: Đại học Xây dựng Hà Nội - trang thông tin tuyển sinh
- Mục tiêu được nhắc tới: học bổng du học
- Trạng thái thu thập: thiếu thông tin chi tiết để phân tích điều kiện và mức hỗ trợ

> Đây là một tài liệu rút gọn, phản ánh đúng dữ liệu thu được từ nguồn, không bổ sung thông tin ngoài trang gốc.
""",
    "viasm-sigma-gold-scholarship.md": """---
doc_id: \"viasm-sigma-gold-scholarship\"
title: \"Học bổng Sigma Gold năm học 2026-2027 cho sinh viên ngành Toán - VIASM\"
source_url: \"https://viasm.edu.vn/hoat-dong-khoa-hoc/tin-tuc/chi-tiet/hoc-bong-sigma-gold-nam-hoc-2026-2027-cho-sinh-vien-nganh-toan\"
retrieved_at: \"2026-09-19\"
document_version: \"2026-2027\"
audience: \"student\"
department: \"financial-aid\"
category: \"scholarships\"
language: \"vi\"
---

# Học bổng Sigma Gold năm học 2026-2027 cho sinh viên ngành Toán - VIASM

Năm học 2026-2027, Viện Nghiên cứu cao cấp về Toán (VIASM) triển khai xét, cấp học bổng Sigma dành cho sinh viên đại học chính quy ngành Toán thuộc các cơ sở giáo dục đại học trên cả nước.

## 1. Đối tượng

- Sinh viên trình độ đại học hệ chính quy thuộc Chương trình đào tạo cử nhân tài năng ngành Toán học của Trường Đại học Khoa học Tự nhiên, Đại học Quốc gia Hà Nội và Trường Đại học Khoa học Tự nhiên, Đại học Quốc gia thành phố Hồ Chí Minh;
- Sinh viên trình độ đại học hệ chính quy ngành Toán học và Sư phạm Toán học thuộc các cơ sở giáo dục đại học tại Việt Nam.

## 2. Nguyên tắc chung

- Học bổng Sigma Gold chỉ áp dụng đối với sinh viên từ khóa tuyển sinh năm 2026 trở đi.
- Sinh viên trong các chương trình cử nhân tài năng ngành Toán học vẫn có thể nộp hồ sơ xét, cấp học bổng Sigma Gold; trong trường hợp được cấp, họ sẽ nhận học bổng và sinh hoạt phí ở mức cao nhất.
- Đối với sinh viên ngành Sư phạm Toán học được hỗ trợ sinh hoạt phí theo các quy định hiện hành, nếu đủ điều kiện được cấp học bổng Sigma Gold thì sẽ được bù phần chênh lệch giữa mức học bổng Sigma Gold và mức hỗ trợ theo quy định.

## 3. Mức học bổng và thời gian cấp

- Mức học bổng: 15 triệu đồng/tháng
- Học bổng được xét theo năm học và cấp theo hai đợt: học kỳ 1 và học kỳ 2
- Mỗi học kỳ cấp 5 tháng, mỗi năm học cấp 10 tháng
- Mỗi sinh viên được xét cấp không quá 8 học kỳ trong toàn khóa học

## 4. Số lượng học bổng

- Tối đa 10 suất

## 5. Hồ sơ yêu cầu

- Công văn và danh sách sinh viên đề nghị xét, cấp học bổng học kỳ 1 của cơ sở giáo dục đại học
- Đối với sinh viên năm thứ nhất:
  - bản sao học bạ năm học lớp 12;
  - bản sao giấy chứng nhận đạt giải nhất, nhì trong kỳ thi học sinh giỏi cấp tỉnh/thành phố trực thuộc Trung ương trở lên ở cấp THPT
- Các thành tích trong học tập và các giải thưởng quốc tế, quốc gia, cấp tỉnh/thành phố (nếu có)
- Các chứng chỉ học thuật SAT, ACT, A-Level, IB, AP (nếu có)
- Bài luận về một định lý, khái niệm, ý tưởng hoặc ứng dụng toán học, dài tối đa 4 trang A4, viết bằng tiếng Anh hoặc tiếng Việt, gửi kèm file LaTeX nguồn và bản PDF

## 6. Thông tin liên hệ

Cô Trần Thùy Linh, chuyên viên Viện NCCCT
Email: Sigma.Scholarship@viasm.edu.vn
""",
    "vnua-k71-freshman-scholarship.md": """---
doc_id: \"vnua-k71-freshman-scholarship\"
title: \"Xét học bổng tân sinh viên K71 - Học viện Nông nghiệp Việt Nam\"
source_url: \"https://vnua.edu.vn/thong-bao/xet-hoc-bong-tan-sinh-vien-k71-58369\"
retrieved_at: \"2026-09-19\"
document_version: \"K71\"
audience: \"student\"
department: \"financial-aid\"
category: \"scholarships\"
language: \"vi\"
---

# Xét học bổng tân sinh viên K71 - Học viện Nông nghiệp Việt Nam

Trang thông báo của Học viện Nông nghiệp Việt Nam về xét học bổng tân sinh viên K71 hiện chỉ hiển thị tiêu đề nguồn và không có nội dung chi tiết được crawl thành công trong bản dữ liệu thu được.

## Ghi chú

- Mục tiêu: xét học bổng cho tân sinh viên K71
- Nguồn: Học viện Nông nghiệp Việt Nam
- Trạng thái thu thập: thiếu mô tả điều kiện, mức học bổng và thời hạn xét tuyển trong trang trả về

> Nội dung dưới đây giữ nguyên thông tin khả dụng từ tài liệu thu được, không bổ sung dữ liệu không có trong nguồn gốc.
""",
}

for name, content in files.items():
    path = folder / name
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path}")
