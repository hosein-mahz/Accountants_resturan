import db_lib 
import log_lib


user_db_address = "db/user_admin"

def user_write(lname , fname , email , password):
    msg = []
    msg.append(db_lib.Id_define())
    msg.append(lname)
    msg.append(fname)
    msg.append(email)
    msg.append(str(password))
    msg.append(db_lib.Date_now)
    deta =",".join(msg)
    deta = deta +"\n"
    
    log_lib.Log("The user is complete")

    db_lib.Writeinfile(deta,user_db_address)


