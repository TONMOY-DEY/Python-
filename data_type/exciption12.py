try:
    a=int(input("Enter the number a :"))
    b=int(input("Enter the number b :"))
    res=a/b
    print("Division:",res)

except ValueError:
    print("a and b must be integer🤗")

except ZeroDivisionError:
    print("Value of b can not be 0")

except:
    print("Something went wrong")