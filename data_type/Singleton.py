class Singleton:
    _object= None

    def __new__(cls):
        if cls._object is None:
          cls._object = super().__new__(cls)
          print("created new object")
        return cls._object

obj1=Singleton()
obj2=Singleton()
obj3=Singleton()

print(obj1 is obj2)
