class Driver:
    def __init__(self,name):
        self.name=name

class Car:
    def __init__(self,name,driver):
        self.name=name
        self.driver=driver

driver=Driver("Mr sikto")
carobj=Car("Marcedes",driver)


print(carobj)
        
