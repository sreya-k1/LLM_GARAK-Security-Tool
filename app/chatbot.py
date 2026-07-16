import ollama

def get_response(user_message: str):

    response = ollama.chat(
        model="gemma2:2b",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response["message"]["content"]