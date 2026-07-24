from template import chat_with_system_prompt


QUESTION = "Giải thích blockchain là gì?"

TEACHER_PERSONA = "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
FINANCE_PERSONA = "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."


def print_result(title: str, persona: str) -> None:
	response, latency = chat_with_system_prompt(persona, QUESTION)
	print(title)
	print("-" * len(title))
	print(f"Persona : {persona}")
	print(f"Latency : {latency:.2f}s")
	print(f"Length  : {len(response)} characters")
	print("Response:")
	print(response)
	print()


def main() -> None:
	print("Cau hoi:")
	print(QUESTION)
	print()

	print_result("Persona 1 - Giao vien tieu hoc", TEACHER_PERSONA)
	print_result("Persona 2 - Chuyen gia tai chinh", FINANCE_PERSONA)

if __name__ == "__main__":
	main()
