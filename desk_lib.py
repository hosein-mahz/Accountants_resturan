import db_lib
import log_lib


desk_db_addresss = "db/nema_desk.txt"

def desk_write( nema ):
    msg = []
    msg.append(db_lib.Id_define())
    msg.append(str(nema))
    deta =",".join(msg)
    deta = deta + "\n"

    log_lib.Log("The desk is complete")
    
    db_lib.Writeinfile(deta,desk_db_addresss)


