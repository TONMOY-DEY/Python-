# a=[1,2,3,4,5]
# result=0


# i=0
# n=len(a)
# while i<n:
#     result=result +a [i]
#     i=i+1
#     print(result)



#problem solving 

a=[-10,2,19,-3,-5]  #[0,2,19,0,0]

i=0
while i<len(a):
    if a[i] < 0:
        a[i] = 0
    i=i+1
    print(a)