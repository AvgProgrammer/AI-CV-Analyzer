class JobApplication:
    def __init__(self, id:int, name:str, email_contact:str, description:str, requirements:list):
        self.id=id
        self.name=name
        self.email_contact=email_contact
        self.description=description
        self.requirements=requirements
    
    def addRequerment(self,new_requerment):
        self.requerment.append(new_requerment)