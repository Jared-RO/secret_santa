from fastapi import FastAPI
from core import run_secret_santa

app = FastAPI()


@app.get("/run")
def run():
    result = run_secret_santa()
    return {
        "status": "ok",
        "assignments": result,
    }
