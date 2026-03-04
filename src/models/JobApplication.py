class JobApplication:
    def __init__(self, name, email_contant, description, requerments):
        self.name=name
        self.email_contant=email_contant
        self.description=description
        self.requerments=requerments
    
    def addRequerment(self,new_requerment):
        self.requerment.append(new_requerment)