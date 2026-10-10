from fastapi import FastAPI

app = FastAPI(
    title="AI Engineering Lab")

@app.get("/")
def home():
    return {
        "message": "Hola mundo",
        "service": "Laboratorio de AI Engineering"
    }

@app.get("/health")
def health():
    return {"status": "ok"}