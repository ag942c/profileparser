from fastapi import FastAPI
import nltk
from src.process import ProcessText
from src.load import model
import time

nltk.download("punkt")  # Download sentence tokenizer
nltk.download("averaged_perceptron_tagger")  # Download POS tagger (lightweight)
nltk.download("maxent_ne_chunker")  # Download chunker for NER
nltk.download('words') # Download words

st = time.time()
list_skill = model.load_skills_model()
list_tech = model.load_technology_model()
list_designation = model.load_designation_model()
end = time.time()

print(f"Model Load time :- {end-st}")


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "All OK !!"}

@app.post("/process")
async def process(text, additional_skills=[], additional_destination=[], additional_tech=[]):
    st = time.time()
    print(f"processing started")
    pt = ProcessText(text, list_skill+additional_skills, list_designation+additional_destination, list_tech+additional_tech)
    output = pt.process()
    end = time.time()
    print(f"processing ended")
    print(f"Total time = {end-st}")
    return output
