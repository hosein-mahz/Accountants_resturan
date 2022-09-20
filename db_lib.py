import random , datetime

def Writeinfile( msg , filenema ):
    w = open(filenema , "a")
    w.write(id_genrator(filenema)+"," + msg +","+Date_now() + ",," +"active"+"\n")
    w.close()


def Readazfile(filenema):
    o = open(filenema, "r")
    db =[]
    for x in o :
        db.append(x.replace("\n",",",1000))
    return db

def Id_searchre(id , filenema):
    o = Readazfile(filenema)
    for x in o :
        x = x.split(",")
        if x[0] == str(id):
            return x 

def Updateinfile( id, msg , filenema ):
    o = Id_searchre(id , filenema)
    if o[0] == str(id):
        tmp = ",".join(o)
        db = Readazfile(filenema)
        db.remove(tmp)
        w = open(filenema , "w")
        w.write("")
        w.close()
        w = open(filenema , "a")
        msgList = msg.split(",")
        for x in db:
            w.write(x + "\n")
        w.write(str(id) + "," + ",".join(msgList[1:-2]) + ","+ Date_now()+","+msgList[-1] +"\n" )
        w.close()
        
    else :
        print ("this record is not difaind")



def Deleteinfile( id , filenema ):
    o = Id_searchre(id , filenema)
    if o[0] == str(id):
        tmp = ",".join(o)
        db = Readazfile(filenema)
        db.remove(tmp)
        w = open(filenema , "w")
        w.write("")
        w.close()
        w = open(filenema , "a")
        for x in db:
            w.write(x + "\n")
        w.close()

def SoftDelete(id , filenema):
    o = Id_searchre(id , filenema)
    if len(o[0]) > 0 :
        Updateinfile(id ,str(o[0:-1])+",del", filenema )





##############################################################

# def Id_define( ):
#     return str(random.randint(0, 1000))

def Date_now( ) :
    return str(datetime.datetime.now())

def id_genrator( fileneam ):
    o = Readazfile(fileneam)
    max = 0
    for x in o:
        x = x.split(",")
        if int(x[0]) > max :
            max = int(x[0])
    return str(max + 1)