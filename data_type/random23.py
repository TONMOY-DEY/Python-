class Student:
    def set_names(self,f_name,l_name):
        self.first_name=f_name
        self.last_name=l_name

A1=Student()
A1.set_names("Jone","Doe")
print(A1.first_name)
print(A1.last_name)