from groq import Groq

client = Groq(
    api_key="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"
)
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": "write me a code in java to pront hello world"
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
