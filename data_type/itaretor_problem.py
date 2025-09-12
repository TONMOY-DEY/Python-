def fruits_gen():
    s = 0
    i = 1

    while True:
        s=s+i
        i=i+1
        yield s
g=fruits_gen()
print(next(g))