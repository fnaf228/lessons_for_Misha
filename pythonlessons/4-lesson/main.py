MY_INT = 10 # константа
while 1 == 1 : # вечный цикл
    x = input("введите число : ")
    if x.isdigit() : # проверка
        print(int(x) > MY_INT)
    if x == "quit" :
        break # выход из цикла