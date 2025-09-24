class Burger:
    def __init__(self):
        self.parts=[]

    def add_part(self,part):
        self.parts.append(part)

    def show(self):
        for part in self.parts:
            print(part)


class BurgerBuilder:
    def __init__(self):
        self.burger=Burger()


    def add_bun(self):
         self.burger.add_part("Top Bun")
         return self

    def add_chese(self):
        self.burger.add_part("chese")
        return self


    def add_patty(self):
        self.burger.add_part("sauce")
        return self

    def add_bottom_bum(self):
        self.burger.add_part("Bottom Bun")
        return self

    def build(self):
        return self.burger
    

bb=BurgerBuilder()

burger=(
bb
.add_bun()
.add_chese()
.add_patty()
.add_patty()
.add_bottom_bum()
.build()
)

burger=bb.build()
burger.show()
