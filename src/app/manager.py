from models import JobApplication
import json

def read_file(path: str):
    try:
        with open(path, "r") as file:
            new_job_list=[]
            data=file.load()
            id=0
            name=""
            email_contant=""
            description=""
            requerments=[]
            for item in data:
                id=item["id"]
                name=item["name"]
                email_contant=item["email_contant"]
                description=item["description"]
                requerments=item["requerments"]
                new_job=JobApplication(id,name,email_contant,description,requerments)
                new_job_list.append(new_job)
            return new_job_list
    except FileNotFoundError as e:
        print (f"Error occurred: {e}")
    finally:
        print("Read File Finish")
