from superlink import security
import mysql.connector as sqltor
from tabulate import tabulate

security.security_init()
secure = security.isSecured()

if secure==True:
    conn = sqltor.connect(host="localhost", user="root", passwd="root", database="empAttendance")

    if conn.is_connected():
        print("Successfully connected!")

    cursor = conn.cursor()
    print("Today's Employee's Attendance is listed below:\n")
    cursor.execute("select * from empattendance_2022_01_31")
    data = cursor.fetchall()

    #tabulate
    headers = ["SNo", "Employee Name", "Employee ID", "Login Time"]
    print(tabulate(data, headers, tablefmt="grid"))

    conn.close()

    if conn.is_closed():
        print("Connection successfully closed!")