a={'rahim':12 ,'karim':14 ,'fahim':78, 1:[1,2,3,4],2:{3,4,5}}

print(type(a))

for i in a :
    print(i)
    print('................')

    for i in a.values():
        print(i)


    print(a.keys(),a.values())

    print('.....................')

for k,v in a .items():
        print(f"key name : {k}","valuse {v}")

a=[1,2,3]
b=["Mango","Banana","Apple"]

        #{1:"Mango", 2:"Banana" ,3: "Apple"}
print(dict(zip(b,a)))
c=dict(zip(b,a))
print(c['Mango'])

print(dict(zip(a,b)))
d=dict(zip(a,b))
print(d[1])


        







