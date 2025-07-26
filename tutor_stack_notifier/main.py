from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Notification(BaseModel):
    message: str


@app.post("/")  # Changed from /notify to / to be consistent
async def notify(n: Notification):
    # Dummy notification logic
    return {"status": "sent", "message": n.message}


@app.get("/health")
async def health():
    return {"status": "ok"}
