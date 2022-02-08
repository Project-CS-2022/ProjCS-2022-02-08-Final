from superlink import security
import mysql.connector as sqltor
import datetime #Library
from tabulate import tabulate

security.security_init()
secure = security.isSecured()

#_main_
if secure==True:

    conn = sqltor.connect(host="localhost", user="root", passwd="root", database="EmpAttendance")

    if conn.is_connected():
        print("Successfully connected!")

    cursor = conn.cursor(buffered=True)  #Enabled buffering
    date = str(datetime.date.today()) #Changing date into string to avoid errors

    #date.replace is used here because to create good looking name of the table with underscore
    cursor.execute("CREATE TABLE IF NOT EXISTS EmpAttendance_{}(SNo integer(2),EmployeeName varchar(30),EmployeeID integer(5),LoginTime varchar(8))".format(date.replace("-","_")))

    TotList = []

    while True:
        #Setup to stop taking attendance by breaking loop
        EmpList = [] #nested list
        cursor.execute("SELECT * FROM EmpAttendance_{}".format(date.replace("-","_")))
        TotAttendance = cursor.rowcount + 1

        Name = input("Your Name:")
        if Name.lower()=="stop":
            print("\tOkay. Stopped taking Attendance!")
            break
        EmpId = int(input("Your Employee ID:"))
        now = datetime.datetime.now()
        CTime = now.strftime("%H:%M:%S") #sorting time into string
        EmpList = [TotAttendance, Name, EmpId, CTime]
        cursor.execute("INSERT INTO EmpAttendance_{} VALUES({},'{}',{},'{}')".format(date.replace("-","_"),TotAttendance,Name,EmpId,CTime))
        conn.commit()
        print("You may go in! Recorded in database")
        TotList.append(EmpList)

    #tabulate module
    headers = ["SNo", "Employee Name", "Employee ID", "Login Time"]
    print("Attendance in memory:\n") #Collects the data of last run by using list
    print(tabulate(TotList, headers, tablefmt="grid"))


    conn.close()

    if conn.is_closed():
        print("Connection successfully closed!")
