import mysql.connector as sqltor
import random
import array
import os
import pyperclip
import time

#requires existing table employees_credential in MySQL

conn = sqltor.connect(host="localhost", user="root", passwd="root", database="sadn")

if conn.is_connected():
    print("Successfully connected!")

#Initiating cursor duties
cursor = conn.cursor()
cursor.execute("SELECT * FROM EMPLOYEES_CREDENTIAL")
fetch = cursor.fetchall()


#Generate Random Token if Employee forgets the password
length = 20
DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9','0']
SYMBOLS = ['.', '@', '#', '$', '%', '=', ':', '?', '~', '*']
LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y','z']
UPPER = []

for i in LOWER:
    if i.islower():
        UPPER.append(i.upper())

#All the above lists combines to get a single list(Array)
COMBINED = DIGITS + SYMBOLS + LOWER + UPPER

#mix random to generate token
mixdigit = random.choice(DIGITS)
mixsymbol = random.choice(SYMBOLS)
mixlower = random.choice(LOWER)
mixupper = random.choice(UPPER)

#making it lengthy to get 20 digit token
passing = mixdigit + mixsymbol + mixupper + mixlower

for x in range(length - 4):
    passing = passing + random.choice(COMBINED)
    passing_list = array.array('u', passing)
    random.shuffle(passing_list)

token = ""
for i in passing_list:
    token += i

#Asking Credentials
name = input("Name of the new Employee:")
passwd = input("Enter fresh password for new Employee, ("+ name+")\n(Requirements: 8+ Characters and must be Alphanumeric):")

if len(passwd)<=7:
    print("[ERROR] Password length must be 8 characters or more")
elif passwd.isalpha() == True:
    print("[ERROR] Password must be Alphanumeric")
elif passwd.isalpha() != True and len(passwd)>=8:
    TotEmployees = cursor.rowcount + 1  #Will calculate the amount of employees and add 1 greater serial no. for new emp
    cursor.execute("INSERT INTO EMPLOYEES_CREDENTIAL VALUES({},'{}','{}','{}')".format(TotEmployees, name, passwd, token))
    conn.commit()
    print("Password has been successfully saved in the database for safety purpose!")
    print("\n\nTOKEN: {}".format(token))
    print("\n\nWARNING: Note the above token and keep it in safer environment. It will be useful incase if you MISS THE PASSWORD!")


    #Using Pyperclip and os modules to open and paste token in a notepad file
    flags = os.O_RDWR | os.O_CREAT
    mode = 0o666  #default mode to open files
    statement = "Username: {}\nTOKEN: {}\n\nCONFIDENTIAL: Note the above token and keep it in a safe directory by clicking File --> Save As. \n\nInfo: This file has been saved and opened by Python software!".format(name, token)
    pyperclip.copy(statement)
    path = "C:\\Users\\DELL\\Desktop\\CS Proj\\{}'s Token".format(name)
    fd = os.open(path, flags, mode)
    os.write(fd, pyperclip.paste().encode())
    #To avoid "File not found" error, Python interpreter will wait and open the file after 2 seconds
    time.sleep(2)
    os.startfile(path)
else:
    print("Your password does not satisfy the requirements! Please run the configuration again.")

conn.close()

if conn.is_closed():
    print("Connection successfully closed!")