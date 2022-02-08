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
    cnt = int(input('With how many of the collaborators did our shares gained and lost [Today]? '))
    TotList = []
    for i in range(cnt):
        name = input('Enter the name of the collaborator: ')
        shares_gained = int(input('Enter the shares gained today?'))
        shares_lost = int(input('Enter the shares lost today?'))
        cursor.execute("Update collaborators Set SharesGained = {}, SharesLost = {} where Name = '{}'".format(shares_gained,shares_lost,name))
        conn.commit()

    strt = 'select*from Collaborators'
    cursor.execute(strt)
    data1 = cursor.fetchall()
    for row in data1:
        print(row)
        TotList.append(row)

    #tabulate module
    headers = ["SNo", "Collaborator", "Shares Gained", "Shares Lost"]
    print("\nCollaborators [Updated today]:\n")
    print(tabulate(TotList, headers, tablefmt="grid"))

    conn.close()

    if conn.is_closed():
        print("Connection successfully closed!")
    
        


