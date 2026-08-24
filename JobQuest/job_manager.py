from application import JobApplication
from file_manager import load_jobs, save_jobs
from datetime import datetime

def add_application():
    print("\n--- Add Job Application ---")
    company = input("Enter company name: ")
    role = input("Enter job role: ")
    location = input("Enter location: ")
    date = datetime.now().strftime("%d-%m-%Y")

    job = JobApplication(company, role, location, date)
    jobs = load_jobs()
    jobs.append(job.to_dictionary())
    save_jobs(jobs)
    print("\nJob application added successfully!")

def view_applications():
    jobs = load_jobs()
    if not jobs:
        print("\nNo job applications found.")
        return

    print("\n--- Your Job Applications ---")
    for number, job in enumerate(jobs, start=1):
        print(f"\nApplication #{number}")
        print(f"Company  : {job['company']}")
        print(f"Role     : {job['role']}")
        print(f"Location : {job['location']}")
        print(f"Date     : {job['date']}")
        print(f"Status   : {job['status']}")
        print("-" * 35)

def search_application():
    search_company = input("\nEnter company name to search: ").lower()
    jobs = load_jobs()
    found = False

    for job in jobs:
        if search_company in job["company"].lower():
            print("\nApplication Found")
            print("-" * 30)
            print("Company :", job["company"])
            print("Role    :", job["role"])
            print("Location:", job["location"])
            print("Date    :", job["date"])
            print("Status  :", job["status"])
            found = True

    if not found:
        print("No application found.")

def update_status():
    company = input("\nEnter company name: ").lower()
    jobs = load_jobs()

    for job in jobs:
        if job["company"].lower() == company:
            print("\nCurrent status:", job["status"])
            print("""
1. Applied
2. Online Assessment
3. Interview
4. Selected
5. Rejected
""")
            choice = input("Select new status: ")
            statuses = {
                "1": "Applied",
                "2": "Online Assessment",
                "3": "Interview",
                "4": "Selected",
                "5": "Rejected"
            }

            if choice in statuses:
                job["status"] = statuses[choice]
                save_jobs(jobs)
                print("Status updated successfully!")
            else:
                print("Invalid status.")
            return

    print("Company not found.")

def delete_application():
    company = input("\nEnter company name to delete: ").lower()
    jobs = load_jobs()
    updated_jobs = [job for job in jobs if job["company"].lower() != company]

    if len(updated_jobs) == len(jobs):
        print("Application not found.")
        return

    save_jobs(updated_jobs)
    print("Application deleted successfully!")
