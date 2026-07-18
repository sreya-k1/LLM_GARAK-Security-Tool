import ollama


def validate_prompt(prompt):
    response = ollama.generate(
        model="llama-guard3",
        prompt=prompt
    )

    return response["response"]