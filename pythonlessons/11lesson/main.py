s = input("введите число: ")
print(s.isdigit())
try:
    x = int(input("введите число: "))
except:
    print("ты уверен?")

try:
    y = int(input("введите число: "))
except:
    print("ты дурак?")

try:
    print(x / y)
except:
    print("не могу поделить")
