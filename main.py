from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from llm_agent import get_department_recommendation

app = FastAPI()

class PatientRequest(BaseModel):
    gender: str
    age: int
    symptoms: List[str]

@app.post("/recommend")
def recommend(payload: PatientRequest):
    info = payload.dict()
    recommended = get_department_recommendation(info)
    return {"recommended_department": recommended}
