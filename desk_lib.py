import db_lib
import log_lib
import random , datetime

desk_db_addresss = "db/nema_desk.txt"

def desk_write( nema ):
    msg = []
    msg.append(id_define())
    msg.append(str(nema))
    deta =",".join(msg)
    deta = deta + "\n"

    log_lib.Log("The desk is complete")
    
    db_lib.Writeinfile(deta,desk_db_addresss)

def id_define( ):
    return str(random.randint(0,100))
