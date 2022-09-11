import os

log_fili_address = "log/Log.txt"
 
def Log(msg):
    if os.environ["LEVEL"] == "prod":
        x = open(log_fili_address,"a")
        x.write(msg + "\n")
        x.close()
    else:
        print(msg)

def Log_debug(msg):
    if os.environ["LEVEL"] != "prod":
        if os.environ["DEBUG_FILE"] == "ture":
            x = open(log_fili_address,"a")
            x.write(msg + "\n")
            x.close()
        else:
            print(msg)