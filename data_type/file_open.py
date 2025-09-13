f=open("data_type/Tonmoy.txt","r")

contant=f.read()

print(contant)
f.seek(0)
print(contant)
f.close()
