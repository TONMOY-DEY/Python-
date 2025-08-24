a=[1,10,23,24,26,90]

result=[]

for i in a:
    if  i%2==0:
        result.append(i)
        print(result)

print('.................................')
#using list comprehension

new_result=[ i for i in a if i%2==0]
print(new_result)


b=[1,2,3,4,5]
result=[ i**2 if i%2==0 else i for i in b]
print(result)




 
        

