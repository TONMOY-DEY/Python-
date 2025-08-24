a=[1,2,3,4,"a",5,6,7]
print(type('a'))
for i in a:
    if type(i)==type('a'):
        break #loop stop kora 
    else:
        print(i)

print('..........')
for i in a:
    if type(i)==type('a'):
        continue #ignore kortechi
    else:
        print(i)