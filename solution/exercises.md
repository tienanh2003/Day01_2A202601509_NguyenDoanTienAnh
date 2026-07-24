# K3 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 9h00–13h00
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng đánh dấu bằng câu trả lời thật
(chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**
**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Temperature 0.0: Một sự thật thú vị về Việt Nam là đất nước này có một hệ thống hang động tự nhiên lớn nhất thế giới, đó là hang Sơn Đoòng. Hang Sơn Đoòng nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng, tỉnh Quảng Bình. Hang động này được phát hiện vào năm 1991 bởi một người dân địa phương tên là Hồ Khanh, nhưng mãi đến năm 2009 mới được công bố rộng rãi sau khi một đoàn thám hiểm người Anh tiến hành khảo sát. Hang Sơn Đoòng có kích thước khổng lồ, với chiều dài hơn 5 km, cao 200 m và rộng 150 m, đủ lớn để chứa cả một tòa nhà chọc trời 40 tầng. Bên trong hang có cả một hệ sinh thái riêng biệt với rừng cây, sông ngầm và các loài động thực vật độc đáo. (latency: 5.49s) Temperature 0.5: Một sự thật thú vị về Việt Nam là đất nước này có hang động lớn nhất thế giới, được gọi là Hang Sơn Đoòng. Hang Sơn Đoòng nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng, tỉnh Quảng Bình. Hang động này được phát hiện vào năm 1991 bởi một người dân địa phương tên là Hồ Khanh, nhưng mãi đến năm 2009 mới được công nhận và thám hiểm bởi một nhóm các nhà thám hiểm người Anh. Hang Sơn Đoòng có một hệ sinh thái riêng biệt, bao gồm cả rừng cây và sông ngầm, và có những khoang hang đủ lớn để chứa cả một tòa nhà chọc trời 40 tầng. Đây là một điểm đến hấp dẫn cho những người yêu thích phiêu lưu và khám phá thiên nhiên. (latency: 5.89s) .Temperature 1.0: Một sự thật thú vị về Việt Nam là hệ thống hang động Phong Nha-Kẻ Bàng ở tỉnh Quảng Bình. Đây là một trong những khu vực có hệ thống hang động phong phú và đa dạng nhất thế giới. Đặc biệt, hang Sơn Đoòng, nằm trong khu vực này, được công nhận là hang động lớn nhất thế giới. Sơn Đoòng có những khoảng không gian lớn đến mức có thể chứa cả một tòa nhà chọc trời 40 tầng, và trong hang còn có cả rừng và sông ngầm. Hệ thống hang động Phong Nha-Kẻ Bàng đã được UNESCO công nhận là Di sản Thế giới vào năm 2003 nhờ giá trị địa chất, địa mạo độc đáo. (latency: 2.83s). Temperature 1.5: Một sự thật thú vị về Việt Nam là đất nước này là nơi sản xuất và xuất khẩu hạt tiêu đen lớn nhất thế giới. Việt Nam chiếm hơn 40% sản lượng hạt tiêu toàn cầu, đóng vai trò quan trọng trong thị trường gia vị thế giới. Hạt tiêu từ Việt Nam nổi tiếng với chất lượng cao và được sử dụng rộng rãi trong ẩm thực toàn cầu. Việc trồng hạt tiêu thường diễn ra ở các tỉnh miền Trung và miền Nam, nơi có khí hậu và thổ nhưỡng phù hợp để phát triển loại cây này. (latency: 6.09s) 

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Sẽ chọn temperature thấp (0.0–0.5) vì đây là những câu trả lời ổn định đúng nội dung sản phẩm.

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> Với cùng một lượng token, chi phí của GPT-4o cao hơn GPT-4o-mini khoảng 16,7 lần. Vì vậy, GPT-4o-mini phù hợp với các tác vụ lặp lại, hỏi đáp thông thường hoặc khi cần tối ưu chi phí. Trong khi đó, GPT-4o phù hợp với các bài toán đòi hỏi khả năng suy luận phức tạp, độ chính xác cao hoặc các tác vụ có mức độ rủi ro lớn.
---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> Phản hồi của persona giáo viên tiểu học ngắn hơn, dùng từ đơn giản và ví blockchain với các hộp đồ chơi để trẻ dễ hình dung. Phản hồi của persona chuyên gia tài chính dài và chi tiết hơn, sử dụng nhiều thuật ngữ như sổ cái phân tán, node, hash và decentralization. System prompt giúp định hướng cách diễn đạt, mức độ chuyên sâu và loại ví dụ mà mô hình sử dụng. Vì vậy, cùng một câu hỏi nhưng mô hình có thể tạo ra hai kiểu trả lời rất khác nhau.


### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> Với tiếng Việt, số token theo `count_tokens` thường cao hơn đáng kể so với ước lượng `số từ / 0.75`, và mức chênh có thể lên tới khoảng 30–60% tùy đoạn văn. Lý do là tiếng Việt có nhiều từ ghép tách bằng dấu cách, dấu thanh và cách mã hóa của tokenizer không luôn khớp với “một từ = một token” như cách đếm thô. Vì vậy, cùng độ dài văn bản, tiếng Việt thường sinh ra nhiều token hơn tiếng Anh.

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming phù hợp khi phản hồi dài hoặc cần giảm cảm giác chờ đợi, vì người dùng thấy kết quả xuất hiện ngay lập tức. Non-streaming phù hợp với các câu trả lời ngắn hoặc khi cần xử lý xong toàn bộ kết quả rồi mới hiển thị.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Exponential backoff giúp giảm áp lực lên API khi hệ thống đang quá tải bằng cách tăng dần thời gian chờ giữa các lần retry. Nếu hàng nghìn client đều retry với cùng một khoảng thời gian cố định, chúng có thể gửi yêu cầu đồng loạt và khiến API tiếp tục bị quá tải.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> System prompt: “Bạn là trợ giảng AI thân thiện, trả lời ngắn gọn, rõ ràng bằng tiếng Việt và ưu tiên đưa ví dụ khi cần.” Mình yêu cầu “trả lời ngắn gọn” để người dùng dễ đọc và “bằng tiếng Việt” để câu trả lời thống nhất với nhóm người dùng mục tiêu.


### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Hạn chế lớn nhất là chatbot chỉ lưu lịch sử 3 lượt nên dễ quên ngữ cảnh của cuộc trò chuyện dài. Có thể cải thiện bằng cách lưu lịch sử vào cơ sở dữ liệu hoặc tóm tắt các lượt hội thoại cũ để mô hình vẫn giữ được ngữ cảnh mà không vượt quá giới hạn token.

---

## Danh Sách Kiểm Tra Nộp Bài

- [ ] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [ ] Cả 4 checkpoint pytest đều pass
- [ ] Tất cả 9 câu trong file này đã được trả lời
- [ ] Đã copy bài làm vào folder `solution/` và zip theo hướng dẫn README
