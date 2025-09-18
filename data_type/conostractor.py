class Student2:
    def __init__(self, f_name, l_name):
        self.first_name = f_name   # instance variable
        self.last_name = l_name

    def get_full_name(self):
        print(f"{self.first_name} {self.last_name}")


# Create objects
A1 = Student2("John", "Doe")
B2 = Student2("Awesome", "Student")

# Call methods
A1.get_full_name()   # John Doe
B2.get_full_name()   # Awesome Student
