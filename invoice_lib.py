import db_lib
import log_lib
import datetime , random

invoice_db_address ="db/invoice.txt"

def invoice_wriet(product,Number,desk):
    msg = []
    msg.append(id_define())
    msg.append(str(desk))
    msg.append(product)
    msg.append(str(Number))
    msg.append(date_now())
    deta =",".join(msg)
    deta = deta + "\n"

    log_lib.Log("The data is complete")
    
    db_lib.Writeinfile(deta,invoice_db_address)


def id_define( ):
    return str(random.randint(0, 1000))

def date_now( ) :
    return str(datetime.datetime.now())