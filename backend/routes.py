from fastapi import APIRouter
from pydantic import BaseModel
from llm_service import generate_question, evaluate_answer

router = APIRouter()

class AnswerRequest(BaseModel):
    answer: str


@router.get("/question")
def get_question(topic: str):
    return {"question": generate_question(topic)}


@router.post("/evaluate")
def evaluate(data: AnswerRequest):
    return evaluate_answer(data.answer)