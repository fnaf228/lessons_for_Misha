# def print_weather() :
#     pass
#
# def get_weather() :
#     pass
#
# def get_city() :
#     return "moscow"
#
# def cat() :
#     pass
#
#
#
# get_city()
# get_weather()
# print_weather()

class Car() :
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year
        self.x = 0
        self.y = 0

    def move(self, x, y) :
        self.x = x
        self.y = y


car1 = Car("BMW", "red", 2016)

car2 = Car("Mercedes", "black", 2020)
car2.x = 4
car2.y = 9
car2.move(4, 9)

cat = "3"
print(type(cat))
print(cat.)

print(car1.color)
print(car1.x, car1.y)
