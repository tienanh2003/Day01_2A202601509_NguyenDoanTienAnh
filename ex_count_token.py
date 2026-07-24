from template import count_tokens, OPENAI_MODEL


VIETNAMESE_SENTENCES = [
	"Việt Nam là một quốc gia có bề dày lịch sử, văn hóa đa dạng và nhiều cảnh quan thiên nhiên đẹp.",
	"Hà Nội là thủ đô của Việt Nam và nổi tiếng với phố cổ, hồ Gươm cùng nhiều món ăn truyền thống.",
	"Trí tuệ nhân tạo đang được ứng dụng rộng rãi trong giáo dục, y tế và kinh doanh ở Việt Nam.",
	"Buổi sáng ở Đà Lạt thường se lạnh, rất thích hợp để thưởng thức một ly cà phê nóng.",
	"Đọc sách mỗi ngày giúp mở rộng vốn từ, tăng khả năng tư duy và cải thiện sự tập trung.",
]


ENGLISH_SENTENCES = [
	"Vietnam is a country with a long history, diverse culture, and many beautiful natural landscapes.",
	"Hanoi is the capital of Vietnam and is known for its old quarter, Hoan Kiem Lake, and traditional food.",
	"Artificial intelligence is being widely used in education, healthcare, and business.",
	"Mornings in Da Lat are often cool, which makes them perfect for a hot cup of coffee.",
	"Reading every day helps expand vocabulary, improve thinking, and strengthen focus.",
]


def estimate_word_based_tokens(text: str) -> float:
	words = len(text.split())
	return words / 0.75


def print_report(title: str, sentences: list[str]) -> None:
	print(title)
	print("-" * len(title))
	for sentence in enumerate(sentences, start=1):
		tiktoken_tokens = count_tokens(sentence, model=OPENAI_MODEL)
		word_estimate = estimate_word_based_tokens(sentence)
		diff_pct = ((tiktoken_tokens - word_estimate) / word_estimate) * 100 if word_estimate else 0.0
		print(f"words            : {len(sentence.split())}")
		print(f"tiktoken tokens  : {tiktoken_tokens}")
		print(f"word estimate    : {word_estimate:.2f}")
		print(f"difference       : {diff_pct:+.2f}%")
	print()


def main() -> None:
	print_report("Vietnamese sentences", VIETNAMESE_SENTENCES)
	print_report("English sentences", ENGLISH_SENTENCES)


if __name__ == "__main__":
	main()
