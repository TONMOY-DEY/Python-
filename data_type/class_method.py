class Student:
    first_name = ""
    last_name = ""

    @classmethod
    def tonmoy(cls, first_name, last_name):
        cls.first_name = first_name
        cls.last_name = last_name


Student.tonmoy("Tonmoy", "Dey")

print(Student.first_name)  # Tonmoy
print(Student.last_name)   # Dey
