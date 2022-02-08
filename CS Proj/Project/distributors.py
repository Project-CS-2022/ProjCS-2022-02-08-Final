from superlink import security
import mysql.connector as sqltor
from tabulate import tabulate

security.security_init()
secure = security.isSecured()

if secure==True:
    conn = sqltor.connect(host="localhost", user="root", passwd="root", database="sadn")

    cursor = conn.cursor(buffered=True)
    cursor.execute("CREATE TABLE IF NOT EXISTS DISTRIBUTORS(SNo integer(4),Name_Of_The_Distributor varchar(50),Items_Received varchar(250))")
    TotItm = []

    dist = int(input('How many distributors we\'ve received today? '))
    for i in range(dist):
        cursor.execute("SELECT * FROM DISTRIBUTORS")
        row = cursor.rowcount + 1

        Name = input('Name of the distributor: ')
        Itm = input('Enter the items received (Separated by commas): ')
        cursor.execute("INSERT INTO Distributors VALUES({},'{}','{}')".format(row,Name,Itm))
        list1 = [row, Name, Itm]
        conn.commit()
        print("Successfully Recorded in database")
        TotItm.append(list1)

    headers = ["SNo", " Name of the distributor", "Items Received"]
    print("Distributors acquired today:\n")
    print(tabulate(TotItm, headers, tablefmt="grid"))

                
    conn.close()

    if conn.is_closed():
        print("Connection successfully closed!")