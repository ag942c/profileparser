from fastapi import FastAPI
from src.process import ProcessText
from src.load import nlp, ruler

import time

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "All OK !!"}

@app.post("/process")
async def process(text, additional_skills=[], additional_destination=[], additional_tech=[]):
    st = time.time()
    print(f"processing started")
    pt = ProcessText(text, nlp, ruler, additional_skills, additional_destination, additional_tech)
    output = pt.process()
    end = time.time()
    print(f"processing ended")
    print(f"Total time = {end-st}")
    return output
