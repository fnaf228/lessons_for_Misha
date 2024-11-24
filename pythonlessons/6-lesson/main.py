my_string = "hello"
my_string2 = 'my'
my_string3 = "name"
my_string4 = "is"
my_string5 = "misha"
print(my_string + ", " + my_string2 + " " + my_string3)
my_list = ["red", "car", "house"]
for x in range(3) :
    print("hello", x)
    my_list[x] += " good"
    print(my_list[x])

misha_list = ["red", 1, -1, "house", 0.5]
for x in range(len(misha_list)) :
    print(type(misha_list[x]) == str)
    if (type(misha_list[x]) == str) :
        misha_list[x] += "good"
    if (type(misha_list[x]) == int) :
        misha_list[x] += 1
print(misha_list)

car_list = ["red-car", "misha-car", "school-car"]
for car in car_list :
    print(car.index("a"))


