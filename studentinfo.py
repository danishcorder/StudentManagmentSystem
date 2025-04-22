class Student:
    def __init__(self, name, roll_number, course,instructor):
        self.name = name
        self.roll_number = roll_number
        self.course = course
        self. instructor=instructor

    def display_info(self):
        print("----- Student Information -----")
        print(f"Name       : {self.name}")
        print(f"Roll No.   : {self.roll_number}")
        print(f"Course     : {self.course}")
        print(f"Instructor  :{self.instructor}) 
        print("-------------------------------")

# Example usage
if __name__ == "__main__":
    student1 = Student("Muhammad Danish", "BSM-2023-16", "Mathematics")
    student1.display_info()
    
