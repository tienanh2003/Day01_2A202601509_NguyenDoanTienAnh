from template import call_openai 

prompt = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."
response00, latency00 = call_openai(prompt, temperature=0.0)
response05, latency05 = call_openai(prompt, temperature=0.5)
response10, latency10 = call_openai(prompt, temperature=1.0)
response15, latency15 = call_openai(prompt, temperature=1.5)
print(f"Temperature 0.0: {response00} (latency: {latency00:.2f}s)")
print(f"Temperature 0.5: {response05} (latency: {latency05:.2f}s)")
print(f"Temperature 1.0: {response10} (latency: {latency10:.2f}s)")
print(f"Temperature 1.5: {response15} (latency: {latency15:.2f}s)")