import datetime , random

def Writeinfile( msg , filenema ):
    w = open(filenema , "a")
    msg.append(str(random.randint(0, 1000)))
    msg.append(str(datetime.datetime.now()))
    w.write(msg)
    w.close()


def Readazfile(filenema):
    o = open(filenema, "r")
    db =[]
    for x in o :
        db.append(x.replace("\n",",",1000))
    return db

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
    
