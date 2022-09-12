import db_lib 
import log_lib
import random , datetime

product_db_address = "db/product.txt"

def product_write(nema , cost ,price):
    msg = []
    msg.append(id_define())
    msg.append(nema)
    msg.append(str(cost))
    msg.append(str(price))
    msg.append(date_now())
    deta =",".join(msg)
    deta = deta +"\n"
    
    log_lib.Log("The product is complete")

    db_lib.Writeinfile(deta,product_db_address)


def id_define( ):
    return str(random.randint(0, 50))

def date_now( ) :
    return str(datetime.datetime.now())
