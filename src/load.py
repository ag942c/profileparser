import spacy
import pickle
import time



class LoadModel:
    def __init__(self, spacy_model_type="en_core_web_trf"):
        if spacy_model_type==None:
            raise ValueError(f'spacy model type {spacy_model_type} provided')
        
        self.spacy_model_type = spacy_model_type
        
        # Load Models
        self.nlp = self.load()

        self.skills_model = self.load_skills_model()
        self.technology_model = self.load_technology_model()
        self.designation_model = self.load_designation_model()
        
        # Add ruler
        self.ruler = self.nlp.add_pipe("entity_ruler")
        
    def load(self):    
        nlp = spacy.load(self.spacy_model_type)
        return nlp
    
    def load_skills_model(self):
        with open('src/models/spacy_ruler_skills.pkl', 'rb') as f:
            skills_list = pickle.load(f)
        return skills_list
        

    def load_technology_model(self):
        with open('src/models/spacy_ruler_tech_stack.pkl', 'rb') as f:
            technology_list = pickle.load(f)
        return technology_list
    
    def load_designation_model(self):
        with open('src/models/spacy_ruler_designation.pkl', 'rb') as f:
            designation_list = pickle.load(f)
        return designation_list
    
    def add_skills(self):
        self.ruler.add_patterns(self.skills_model)
        return self.nlp, self.ruler

    def add_technology(self):
        self.ruler.add_patterns(self.technology_model)
        return self.nlp, self.ruler

    def add_designation(self):
        self.ruler.add_patterns(self.designation_model)
        return self.nlp, self.ruler


st = time.time()
model = LoadModel()
nlp1, ruler1 = model.add_technology()
nlp2, ruler2 = model.add_designation()
nlp, ruler = model.add_skills()
end = time.time()
print(f"Model Load time :- {end-st}")
