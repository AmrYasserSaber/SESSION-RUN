import random

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class sessionHour(BaseModel):
    what_hour_is_the_session: str | int

@app.post("/")
def read_root(body: sessionHour):
    if body.what_hour_is_the_session in ["02:00", "14:00", "2:00", 2, 14]:
        return {
            "message": f"YOU HAVE OPENED THE PORTAL, Take this code {random.randint(200, 505)} and RUN!",
            "topics": [
                "What the hell is backend",
                "How do you communicate with the backend?",
                "API architecture styles",
                "REST APIs",
                "Databases",
                "Deployment"
            ]
        }
    return {"message": f"PORTAL IS CLOSED, TRY A DIFFERENT TIME? !"}