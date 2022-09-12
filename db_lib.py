
def Writeinfile( msg , filenema ):
    w = open(filenema , "a")
    w.write(msg)
    w.close()


def Readazfile(filenema):
    o = open(filenema, "r")
    db =[]
    for x in o :
        db.append(x.replace("\n",",",1000))
    return db

def Id_searchre(id , filenema):
    o = open(filenema,"r")
    for x in id :
        for z in o:
            if x[0] == z[0]:
               return x[0] 

# def Updateinfile( msg , filenema ):
#     o = open(filenema,"r")
#     w = open(filenema,"a")
#     for x in msg:
#         if x[0] == o[0]:
#             if x[] != o[]:
#                 msg = x[] = o[]
#     msg.append(str(datetime.datetime.now()))
#     w.write(msg)
#     w.close()


# def Deleteinfile( msg , filenema ):
#     o = open(filenema,"r")
#     for x in msg:
#         if x[0] == o[0]:
#             x.clear()
#     o.close()
    
def id_define( ):
    return str(random.randint(0, 1000))

def date_now( ) :
    return str(datetime.datetime.now())