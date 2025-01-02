# uvicorn main1:app --reload
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello":"Alankar"}