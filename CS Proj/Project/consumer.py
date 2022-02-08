from superlink import user #importing our own user module from superlink library
import mysql.connector as sqltor
from superlink import security

security.security_init()
secure = security.isSecured()

#_main_
if secure == True:
    conn = sqltor.connect(host="localhost", user="root", passwd="root", database="sadn")

    if conn.is_connected():
        print("Successfully connected!")

    cursor = conn.cursor(buffered=True)
    #Creating table
    cursor.execute("CREATE TABLE IF NOT EXISTS CONSUMERS(SNo integer(8),Name varchar(100),Gender varchar(6), Location varchar(250), Country varchar(50), Email varchar(100), MobileNo varchar(30), RegistredOn varchar(25) )")

    cursor.execute("SELECT * FROM Consumers")
    sno = cursor.rowcount + 1
    name = user.name()
    gender = user.gender()
    location = user.location()
    country = user.country()
    email = user.email()
    mobileno = user.mobileNo()
    regon = user.registeredOn()
    #Inserting Values
    cursor.execute("INSERT INTO CONSUMERS VALUES({},'{}','{}','{}','{}','{}','{}','{}')".format(sno,name,gender,location,country,email,mobileno,regon))
    conn.commit()
    print("Entered!")