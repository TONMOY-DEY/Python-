# fruits=["apple","Banana","Dalim","Orange","Mango"]

# print(fruits[3])

# fruits=["apple","Banana","Dalim","orange","Mango"]

# print(fruits[1][0])

fruits=["apple","banana","Dalim","orange","mango"]

fruit=fruits[2]
c = fruit[3]
print(c)


#Mutable vs Immutable

fruits=["apple","banana","Dalim","orange","mango"]
print(id(fruits))
fruits[3]="pineapple"
print(id(fruits))

