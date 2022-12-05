class Bottle:
    color = str
    contains = bool

    def __init__(self):
        self.contains = 0

    def get_content(self):
        return self.contains

    def fill(self, volume):
        self.contains += volume


bottle_1 = Bottle()
bottle_2 = Bottle()

bottle_1.color = 'Красная'
bottle_2.color = 'Синяя'


print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())

print(bottle_2.color, bottle_2.get_content())
bottle_2.fill(500)
print(bottle_2.color, bottle_2.get_content())
