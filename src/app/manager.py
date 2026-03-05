from src.models.job_application import JobApplication
import json

def read_file(path: str):
    """
    Parameters:
        param1 (str): File path to be uploaded with new job applications.

    Returns:
        list[job_application]: A list of new job applications as job_application objects.
    """
    try:
        with open(path, "r") as file:
            new_job_list=[]
            data=json.load(file)
            id=0
            name=""
            email_contact=""
            description=""
            requirements=[]

            for item in data:
                id=item["id"]
                name=item["name"]
                email_contact=item["email_contact"]
                description=item["description"]
                requirements=item["requirements"]
                new_job=JobApplication(id,name,email_contact,description,requirements)
                new_job_list.append(new_job)
            return new_job_list
    except FileNotFoundError as e:
        print (f"Error occurred: {e}")
    finally:
        print("Read File Finish")

def sentEmail(Email:str,response:str):
    """
    parameters:
        param1 (str): The hiring manager's email for this job application.
        param2 (str): The AI model's response.
    """
    print("an email was sent to",Email)


data_path="data/dummy.json"
new_job_list=read_file(data_path)
print(new_job_list)