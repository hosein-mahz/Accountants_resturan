import db_lib
import log_lib


invoice_db_address ="db/invoice.txt"

def invoice_wriet(product,Number,desk):
    msg = []
    msg.append(db_lib.Id_define())
    msg.append(str(desk))
    msg.append(product)
    msg.append(str(Number))
    msg.append(db_lib.Date_now())
    deta =",".join(msg)
    deta = deta + "\n"

    log_lib.Log("The data is complete")
    
    db_lib.Writeinfile(deta,invoice_db_address)


