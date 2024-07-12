import json
import nltk

class ProcessText:
    def __init__(self, text, skills, designations, techs):
        print(f"Start Processing")
        self.text = text
        self.ents2find = {"DESIGNATIONS":designations, "SKILLS":skills, "TECHS": techs}
    
    def preprocessing(self):
        return self.text.replace(",", "").lower()
    
    def extract_entities(self, text, entnties, sent_id):
        sentences = nltk.sent_tokenize(text)
        for idx, sentence in enumerate(sentences):
            tokens = nltk.word_tokenize(sentence)
            pos_tags = nltk.pos_tag(tokens)
            for chunk in nltk.ne_chunk(pos_tags):
                if type(chunk) == nltk.Tree:
                    if sent_id>5 and chunk.label()=="PERSON":
                        continue
                    ent = " ".join([c[0] for c in chunk.leaves()])
                    if entnties.get(chunk.label()):
                        entnties[chunk.label()] +=[ent]
                    else:
                        entnties[chunk.label()] =[ent]
        return entnties

    def process(self):
        entnties_dict = {}
        for sntid, txt in enumerate(self.text.split("\\n")):
            print(f"--------------> {txt} <-------------")
            entnties_dict = self.extract_entities(txt, entnties_dict, sent_id = sntid)
        self.text = self.preprocessing()
        self.text_list = self.text.split()
        
        entnties_dict["DESIGNATIONS"] = []
        entnties_dict["SKILLS"] = []
        entnties_dict["TECHS"] = []

        for key, value in self.ents2find.items():
            for token in value:
                if len(token.split())>1:
                    if token in self.text:
                        entnties_dict[key] +=[token]
                elif token in self.text_list:
                    entnties_dict[key] +=[token]
        

        
        return entnties_dict

    
