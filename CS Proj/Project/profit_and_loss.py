import mysql.connector as sqltor
from superlink import security
from tabulate import tabulate

security.security_init()
secure = security.isSecured()


if secure == True:

    conn = sqltor.connect(host="localhost", user="root", passwd="root", database="sadn")

    if conn.is_connected():
        print("Successfully connected!")

    cursor = conn.cursor(buffered=True) #Note 1
    cursor.execute("CREATE TABLE IF NOT EXISTS PROFIT_LOSS(SNo integer(4), Category varchar(50),Profit varchar(50), Loss varchar(50))")
    TotList = []
    categ = int(input('Enter the number of categories: '))
    for i in range(1, categ+1):
        cursor.execute("SELECT * FROM PROFIT_LOSS")
        row = cursor.rowcount + 1
        Name = input('Category {}: '.format(i))
        Profit = input('Enter the Profit gained: ')
        Loss = input('Enter the amount we lost: ')
        cursor.execute("INSERT INTO PROFIT_LOSS VALUES({},'{}','{}', '{}')".format(row, Name , Profit , Loss))
        conn.commit()
        list1 = [row, Name, Profit, Loss]
        
        print("Successfully Recorded in database")
        TotList.append(list1)

    #tabulate duties
    headers = ["SNo", "Category", "Profit", "Loss"]
    print("Profit and Loss:\n")
    print(tabulate(TotList, headers, tablefmt="grid"))

    conn.close()
    if conn.is_closed():
        print("Connection successfully closed!")
