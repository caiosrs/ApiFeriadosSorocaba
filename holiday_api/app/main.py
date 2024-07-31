from fastapi import FastAPI
from .holidays import get_holidays

app = FastAPI()

@app.get("/holidays/")
def read_holidays():
    return get_holidays()
