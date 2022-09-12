import db_lib 
import log_lib


product_db_address = "db/product.txt"

def product_write(nema , cost ,price):
    msg = []
    msg.append(db_lib.Id_define())
    msg.append(nema)
    msg.append(str(cost))
    msg.append(str(price))
    msg.append(db_lib.Date_now())
    deta =",".join(msg)
    deta = deta +"\n"
    
    log_lib.Log("The product is complete")

    db_lib.Writeinfile(deta,product_db_address)



