import mysql.connector as sql


try:
# context manager: use for resource allocation
    p=input("Please enter your password :")
    dbCon = sql.connect(host ="localhost", user="root", database ="filmflix", password=p)
    #insert your MySQL Workbench password into line above
    dbCursor = dbCon.cursor(prepared=True)
          
    status="Connection Successful"
    print(status)
    
except sql.errors.Error as e:
    status= f"DB connection failed because: {e}" 
    print(status)
"method 2"
def dbAccess():
    try:
    # context manager: use for resource allocation
        dbCon = sql.connect(host ="localhost", user="root", database ="filmflix", password="")
        dbCursor = dbCon.cursor(prepared=True)
          
        print("Connection successful using Method 2")
   
    except sql.errors.Error as e:
        print(f"DB failed because: {e}") 
    return dbCon, dbCursor
