def fruits_gen():
    fruits=["apple","bananan","mango"]

    for fruit in fruits:
        yield fruit

g=fruits_gen()
print(next(g))
print(next(g))