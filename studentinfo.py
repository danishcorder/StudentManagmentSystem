class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

    def display_info(self):
        print("----- Student Information -----")
        print(f"Name       : {self.name}")
        print(f"Roll No.   : {self.roll_number}")
        print(f"Course     : {self.course}")
        print("-------------------------------")

# Example usage
if __name__ == "__main__":
    student1 = Student("Sania Irshad", "BSM-23-19", "Python Programming")
    student1.display_info()
    