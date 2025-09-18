class Student:
    first_name = "A"
    last_name = "B"

    def set_first_name(self, fname):
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def get_full_name(self):
        print(f"{self.first_name} {self.last_name}")

    @classmethod
    def change_name(cls, first_name, last_name):
        cls.first_name = first_name
        cls.last_name = last_name


# Test
st1 = Student()
st2 = Student()

print("Before change:")
print(st1.first_name, st1.last_name)  # A B
print(st2.first_name, st2.last_name)  # A B

Student.change_name("John", "Doe")


print("\nAfter change:")
print(st1.first_name, st1.last_name)  # John Doe
print(st2.first_name, st2.last_name)  # John Doe
