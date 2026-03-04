class JobApplication:
    def __init__(self, id:int, name:str, email_contant:str, description:str, requerments:list):
        self.id=id
        self.name=name
        self.email_contant=email_contant
        self.description=description
        self.requerments=requerments
    
    def addRequerment(self,new_requerment):
        self.requerment.append(new_requerment)