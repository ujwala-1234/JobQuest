from job_manager import (
    add_application,
    view_applications,
    search_application,
    update_status,
    delete_application
)
from analytics import show_statistics

def display_menu():
    print("\n" + "=" * 45)
    print("       JOBQUEST - JOB APPLICATION TRACKER")
    print("=" * 45)
    print("""
1. Add Job Application
2. View Applications
3. Search Application
4. Update Application Status
5. Delete Application
6. View Job Search Analytics
7. Exit
""")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            search_application()
        elif choice == "4":
            update_status()
        elif choice == "5":
            delete_application()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            print("\nThank you for using JobQuest!")
            print("Good luck with your job search!")
            break
        else:
            print("\nInvalid choice. Please enter 1-7.")

if __name__ == "__main__":
    main()
