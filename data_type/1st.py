#Print all even numbers between 1 and 50. 

result=range(1,50)
for i in result:
 if(i%2==0):
  print(i)

  #using list comprehension
  result1=list(range(1,50))
  result2=[i for i in result1 if i%2==0]
  print(result2)
