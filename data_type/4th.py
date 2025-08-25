#Write a program that prints numbers from 1 to 20, but skip the multiples of 3 using continue.
result=list(range(1,20))

for i in result:
    if i%3==0:
        continue
    else:
        print(i)



