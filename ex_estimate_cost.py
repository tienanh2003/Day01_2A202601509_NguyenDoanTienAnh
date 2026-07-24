
REAL_USERS = 10000
CALLS_PER_USER = 3
OUTPUT_TOKENS_PER_CALL = 350

PRICING_PER_1K_TOKENS = {
	"gpt-4o": {"input": 0.0025, "output": 0.0100},
	"gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
}


def cost_for_call(model: str, input_tokens: int = 0, output_tokens: int = OUTPUT_TOKENS_PER_CALL) -> float:
	pricing = PRICING_PER_1K_TOKENS[model]
	return (input_tokens / 1000) * pricing["input"] + (output_tokens / 1000) * pricing["output"]


def main() -> None:
	total_calls = REAL_USERS * CALLS_PER_USER

	gpt4o_one_call = cost_for_call("gpt-4o")
	mini_one_call = cost_for_call("gpt-4o-mini")

	gpt4o_total = gpt4o_one_call * total_calls
	mini_total = mini_one_call * total_calls
	ratio = gpt4o_total / mini_total if mini_total else float("inf")

	print(f"One-call estimate (output only, {OUTPUT_TOKENS_PER_CALL} tokens):")
	print(f"GPT-4o      : ${gpt4o_one_call:.6f}")
	print(f"GPT-4o-mini : ${mini_one_call:.6f}")
	print()
	print(f"Workload: {REAL_USERS:,} users x {CALLS_PER_USER} calls = {total_calls:,} calls")
	print(f"GPT-4o total      : ${gpt4o_total:.4f}")
	print(f"GPT-4o-mini total : ${mini_total:.4f}")
	print(f"GPT-4o / mini ratio: {ratio:.2f}x")

if __name__ == "__main__":
	main()
