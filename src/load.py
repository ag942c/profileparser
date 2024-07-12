import pickle



class LoadModel:
    def __init__(self):

        self.skills_model = self.load_skills_model()
        self.technology_model = self.load_technology_model()
        self.designation_model = self.load_designation_model()
        
    
    def load_skills_model(self):
        with open('src/models/skills.pkl', 'rb') as f:
            skills_list = pickle.load(f)
        return skills_list
        

    def load_technology_model(self):
        with open('src/models/tech_stack.pkl', 'rb') as f:
            technology_list = pickle.load(f)
        return technology_list
    
    def load_designation_model(self):
        with open('src/models/designation.pkl', 'rb') as f:
            designation_list = pickle.load(f)
        return designation_list
    
    # def add_skills(self, list_skills, additional_skills):
    #     return list_skills + additional_skills

    # def add_technology(self, list_tech, additional_tech):
    #     return list_tech + additional_tech

    # def add_designation(self, list_designation, additional_designation):
    #     return list_designation + additional_designation


model = LoadModel()
