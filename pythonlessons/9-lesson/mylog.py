import datetime

def add_to_log(a:str, to_screen=True, to_disk=True ) :
    if to_disk :
        LOG_NAME = "main.log"
        log_name = open(LOG_NAME, "a", encoding="utf-8")
        log_name.write(str(datetime.datetime.now()) + " : " + a + "\n")
        log_name.close
    if to_screen :
        print(str(datetime.datetime.now()) + " : " + a )
# for x in range(10) :
#     add_to_log(str(x))
