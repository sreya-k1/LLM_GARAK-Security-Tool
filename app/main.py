from fastapi import FastAPI

from app.models import ChatRequest
from app.chatbot import get_response
from app.security import validate_prompt

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to the AI Security Chatbot!"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    if not validate_prompt(request.message):
        return {
            "response": "Prompt rejected by security policy."
        }

    response = get_response(request.message)

    return {
        "response": response
    }