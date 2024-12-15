my_log = open("main.log", "r", encoding="utf-8")
lines = my_log.readlines()
print(lines)

for line in lines :
    print(line, end="")