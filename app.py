from fastapi import FastAPI
from pydantic import BaseModel
from bot_logic import ask_bot

app = FastAPI(title="Real Estate AI Bot Demo")

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(question: Question):
    answer, ticket_needed = ask_bot(question.question)
    return {"answer": answer, "ticket_created": ticket_needed}
