import mysql.connector as sqltor
from superlink import security
from tabulate import tabulate

security.security_init()
secure = security.isSecured()


if secure==True:

    conn = sqltor.connect(host="localhost", user="root", passwd="root", database="sadn")

    if conn.is_connected():
        print("Successfully connected!")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CONSUMERS_SUPPORT")
    data = cursor.fetchall()
    header = ["SNo","Name","Country","MobileNo","Date & Time","Support"]
    print(tabulate(data,header,tablefmt="grid"))

    conn.close()

    if conn.is_closed():
        print("Connection successfully closed!")