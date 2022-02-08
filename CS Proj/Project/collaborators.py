from superlink import security
import mysql.connector as sqltor
from tabulate import tabulate

security.security_init() #Starts monitoring people by asking username/password
secure = security.isSecured() #Boolean

#_main_
if secure==True:

    conn = sqltor.connect(host="localhost", user="root", passwd="root", database="sadn")

    if conn.is_connected():
        print("Successfully connected!")

    cursor = conn.cursor()

    #Creating Table
    cursor.execute("CREATE TABLE IF NOT EXISTS Collaborators(SNo integer(3),Name varchar(30),SharesGained integer(8), SharesLost integer(8))")
    count = int(input('How many collaborators? ' ))
    for i in range(count):
        Name1 = input("Enter the name of the collaborator: ")
        shr1 = int(input('Enter the number of shares gained: '))
        shr2 = int(input('Enter the number of shares lost: '))
        cursor.execute("INSERT INTO Collaborators VALUES({},'{}',{},'{}')".format(i+1,Name1,shr1,shr2))
        conn.commit()
    
    #Reading from Collaborators table and using tabulate
    strt = 'SELECT * FROM Collaborators'
    cursor.execute(strt)
    TotList = []
    data1 = cursor.fetchall()
    for row in data1:
        print(row)
        TotList.append(row)

    headers = ["SNo", "Collaborator", "Shares Gained", "Shares Lost"]
    print("\nCollaborators:\n")
    print(tabulate(TotList, headers, tablefmt="grid"))


    #Closing the connection
    conn.close()

    if conn.is_closed():
        print("Connection successfully closed!")
