from superlink import security
import mysql.connector as sqltor
from tabulate import tabulate

security.security_init()
secure = security.isSecured()

#_main_
if secure == True:
    conn = sqltor.connect(host="localhost", user="root", passwd="root", database="sadn")

    cursor = conn.cursor()
    print("Today's Crypto details:\n")
    cursor.execute("select * from Crypto")
    data = cursor.fetchall()

    #tabulate
    headers = ["SNo", "Price(INR)", "Price"]
    print(tabulate(data, headers, tablefmt="grid"))

    conn.close()
    if conn.is_closed():
        print("Connection successfully closed!")