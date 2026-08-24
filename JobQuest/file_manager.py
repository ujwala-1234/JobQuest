import json

FILE_NAME = "jobs.json"

def load_jobs():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_jobs(jobs):
    with open(FILE_NAME, "w") as file:
        json.dump(jobs, file, indent=4)
