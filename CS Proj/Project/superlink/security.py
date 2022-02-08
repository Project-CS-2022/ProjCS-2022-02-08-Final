import mysql.connector as sqltor

conn = sqltor.connect(host="localhost", user="root", passwd="root", database="sadn")
cursor = conn.cursor()


gate=False

def security_init():
    global gate
    attempt = 1
    while gate==False:
        name = input("Enter your Name: ")
        password = input("Enter your Password: ")
        cursor.execute("select * from employees_credential where (Name='{}') &&Password='{}'".format(name, password))
        data = cursor.fetchone()

        if attempt==3:
            print("You got locked!")
            gate="locked"
            break
        elif data==None:
            print("Your credentials are not matching! You used:",attempt,"/3 attempts. The 4th attempt will not be accepted!")
            attempt += 1
        elif name==data[1] and password==data[2]:
            gate=True
        else:
            print("Failed. Your Name / Password might be case sensitive! You used:",attempt,"/3 attempts. The 4th attempt will not be accepted!")
            attempt += 1

def isSecured():
    return gate