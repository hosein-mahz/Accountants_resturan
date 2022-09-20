import invoice_lib
import desk_lib
import user_lib
import product_lib
import db_lib

# desk_lib.desk_write(3)
# product_lib.product_write("petza", 65000 , 130000)
# user_lib.user_write("hosein","zarie","hoseinmhz986@gmail.com",21398734)
# invoice_lib.invoice_wriet( "pasta" , 1 ,19)

# db_lib.Updateinfile( 27, "27,57,ok,,,sala" ,"db/nema_desk.txt")
# db_lib.Deleteinfile(984 ,"db/nema_desk.txt" )
# db_lib.SoftDelete(984 ,"db/nema_desk.txt" )
print( db_lib.id_genrator("db/nema_desk.txt"))