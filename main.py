import random

from fastapi import FastAPI

app = FastAPI()


@app.post("/")
def read_root():
    return {"message": f"YOU HAVE OPENED THE PORTAL, RUN WITH THIS CODE {random.randint(200,505)} !"}

@app.post("/send-your-cat")
def send_your_cat():
    
    return {"message": f"YOU HAVE OPENED THE PORTAL, RUN WITH THIS CODE {random.randint(200,505)} !"}