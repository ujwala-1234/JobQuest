class JobApplication:
    def __init__(self, company, role, location, date, status="Applied"):
        self.company = company
        self.role = role
        self.location = location
        self.date = date
        self.status = status

    def to_dictionary(self):
        return {
            "company": self.company,
            "role": self.role,
            "location": self.location,
            "date": self.date,
            "status": self.status
        }

    def display(self):
        print(f"Company  : {self.company}")
        print(f"Role     : {self.role}")
        print(f"Location : {self.location}")
        print(f"Date     : {self.date}")
        print(f"Status   : {self.status}")
        print("-" * 40)
