class Student:
    first_name=""
    last_name=""

    def set_first_name(self,fname):
        self.first_name=fname

    def set_last_name(self,fname):
        self.last_name=fname

    def get_full_name(self):
        print(f"{self.first_name} {self.last_name}")


st1=Student()  #Instance mean function oppsite name
st2=Student()

# st1.first_name="John"
# st1.last_name="Doe"

st1.set_first_name("John")
st1.set_last_name("Doe")

st2.first_name="jane"
st2.last_name="Doe"

st1.get_full_name()
st2.get_full_name()