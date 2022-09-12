import db_lib 
import log_lib
import random , datetime

user_db_address = "db/user_admin"

def user_write(lname , fname , email , password):
    msg = []
    msg.append(id_define())
    msg.append(lname)
    msg.append(fname)
    msg.append(email)
    msg.append(str(password))
    msg.append(str(date_now()))
    deta =",".join(msg)
    deta = deta +"\n"
    
    log_lib.Log("The user is complete")

    db_lib.Writeinfile(deta,user_db_address)


def id_define( ):
    return str(random.randint(0, 50))

def date_now( ) :
    return str(datetime.datetime.now())
