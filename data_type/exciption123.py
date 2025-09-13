try:
    a=int(input("Enter the number a :"))
    b=int(input("Enter the number b :"))
    res=a/b
    print("Division:",res)

except Exception as e:
    print(e)