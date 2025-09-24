class Animal:
    def speak(self):
        print("...........")

class Dog(Animal):
    def speak(self):
       print("Gheu gheu!")

class cat(Animal):
    def speak(self):
        print("Mew Mew !")


class AnimalFactory:
    def create_animal(animal_type):
        if animal_type == "dog":
            ob1=Dog()
            return ob1
        elif animal_type == "cat":
            ob2=cat()
            return ob2
        
cat_obj=AnimalFactory.create_animal("cat")
dunki=AnimalFactory.create_animal("dog")

print(dunki)