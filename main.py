from fastapi import FastAPI, Body, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from utils import generate

import json


app = FastAPI()

origins = '*'

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Req(BaseModel):
    prompt: str


@app.post('/gemini')
def run(req: Req):

    response = generate(req.prompt)
    print(">>>>>>", response.text)
    return {"response": response.text}
