from superlink import security
import mysql.connector as sqltor
from tabulate import tabulate

security.security_init()
secure = security.isSecured()

if secure == True:

    conn = sqltor.connect(host="localhost", user="root", passwd="root", database="sadn")

    if conn.is_connected():
        print("Successfully connected!")

    cursor = conn.cursor()
    cnt = int(input('In how many categories did we gained or lost today '))
    TotList = []
    for i in range(cnt):
        Name = input('Enter the name of the category: ')
        Profit_week = int(input('Enter the Profit [INR]'))
        Loss_week = int(input('Enter the Loss [INR]?'))
        #Updating table
        cursor.execute("Update Profit_Loss Set Profit = {}, Loss = {} where Category = '{}'".format(Profit_week,Loss_week,Name))
        conn.commit()

    strt = 'SELECT * FROM Profit_Loss'
    cursor.execute(strt)
    data1 = cursor.fetchall()
    for row in data1:
        TotList.append(row)

    headers = ["SNo", "Category", "Profit", "Loss"]
    print("\nProfit and Loss Data [Updated today]:\n")
    print(tabulate(TotList, headers, tablefmt="grid"))

    conn.close()

    if conn.is_closed():
        print("Connection successfully closed!")
