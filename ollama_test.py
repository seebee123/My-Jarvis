from ollama import chat

response = chat(
    model="qwen2.5:3b",
    messages=[
        {"role": "user", "content": "who are you"}
    ]
)

print(response["message"]["content"])