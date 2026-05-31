from fastapi import FastAPI

app = FastAPI(title="ProcedIA API")

@app.get("/")
def home():
    return {"mensaje": "ProcedIA funcionando"}
