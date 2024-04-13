from fastapi import FastAPI, Body, Response
from fastapi.middleware.cors import CORSMiddleware

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

@app.post('/gemini')
def run(payload: dict = Body(...)):
    prompt = payload.get('prompt')

    if not prompt:
        return {'error': 'Missing prompt in request payload'}

    response = generate(prompt)

    return {response: response}