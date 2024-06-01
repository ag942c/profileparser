import json


class ProcessText:
    def __init__(self, text, nlp, ruler, additional_skills=[], additional_destination=[], additional_tech=[]):
        print(f"Start Processing")
        self.nlp = nlp
        self.ruler = ruler
        self.text = text
        if additional_tech!=[]:
            print(f"Adding Additional Technology")
            self.additional_tech = additional_tech
            self.add_additional_tech()

        if additional_destination!=[]:
            print(f"Adding Additional Designation")
            self.additional_destination = additional_destination
            self.add_additional_designation()

        if additional_skills!=[]:
            print(f"Adding Additional Skills")
            self.additional_skills = additional_skills
            self.add_additional_skills()
            

    def add_additional_skills(self):
        jsnl_li = []
        for skill in self.additional_skills:
            if not skill:
                continue
            pattern = {"label":"SKILL", "pattern":[]}
            #for word in skill.split():
            pattern["pattern"].append({"LOWER": skill.strip()})
            jsnl_li.append(pattern)

        self.ruler.add_patterns(jsnl_li)

    def add_additional_designation(self):
        designation_li = []
        for desig in self.additional_destination:
            if not desig:
                continue
            pattern = {"label":"DESIGNATION", "pattern":[]}
            #for word in desig.split():
            pattern["pattern"].append({"LOWER": desig.strip()})
            designation_li.append(pattern)

        self.ruler.add_patterns(designation_li)

    def add_additional_tech(self):
        tech_stack_li = []
        for tech in self.additional_tech:
            if not tech:
                continue
            pattern = {"label":"TECHNOLOGY", "pattern":[]}
            #for word in tech.split():
            pattern["pattern"].append({"LOWER": tech.strip()})
            tech_stack_li.append(pattern)

        self.ruler.add_patterns(tech_stack_li)

    def preprocessing(self):
        return self.text.replace(",", "").lower()

    def process(self):
        self.text = self.preprocessing()
        doc = self.nlp(self.text)

        output = {}
        for ent in doc.ents:
            if ent.label_ not in output:
                output[ent.label_] = [(ent.text, ent.start_char, ent.end_char)]
            else:
                output[ent.label_].append((ent.text, ent.start_char, ent.end_char))
        
        return output

    
