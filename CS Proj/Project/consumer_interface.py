from random import choice
import mysql.connector as sqltor
from tabulate import tabulate
import time
import datetime

conn = sqltor.connect(host="localhost", user="root", passwd="root", database="sadn")

if conn.is_connected():
    print("✅")

cursor = conn.cursor(buffered=True)

cursor.execute("CREATE TABLE IF NOT EXISTS CONSUMERS_SUBSCRIPTIONS(Recharge_id integer(8),Name varchar(100), MobileNo varchar(30), Plan varchar(250), Beneficials varchar(1000), Subscribed_on varchar(30))")
cursor.execute("CREATE TABLE IF NOT EXISTS CONSUMERS_SUPPORT(SNo integer(8),Name varchar(100), Country varchar(50), MobileNo varchar(30), Date_Time varchar(30), Support varchar(10000))")

#Login Portal
email = input("Enter your E-Mail: ")
mobno = input("Enter your Mobile no: ")

cursor.execute("SELECT * FROM CONSUMERS WHERE (Email='{}') &&MobileNo='{}'".format(email, mobno))
cons = cursor.fetchone()

#To fetch number of rows
cursor.execute("SELECT * FROM CONSUMERS_SUBSCRIPTIONS")
subrows = cursor.rowcount + 1

#Fetch Plans of single user
cursor.execute("SELECT * FROM CONSUMERS_SUBSCRIPTIONS WHERE (Name='{}') &&MobileNo='{}'".format(cons[1], mobno))
topmostPlan = cursor.fetchone() #Fetch topmost and old plan of the user
totalplans = cursor.rowcount
header1 = ["R.ID", "Name", "MobileNo", "Plan", "Beneficials", "Recharged on"]

#Fetch Support table FOR NO. OF ROWS
cursor.execute("SELECT * FROM CONSUMERS_SUPPORT")
fetchspt = cursor.fetchall()
sptrows = cursor.rowcount + 1


if cons==None:
    print("No details found!")
elif email==cons[5] and mobno==cons[6]:
    print("Logged in successfully!\nWelcome to Superlink Dashboard!")
    print("1. Make Payment")
    print("2. View your Plan Details")
    print("3. Manage Subscription(s)")
    print("4. Need help?")
    print("0. Exit")

    try:
        choice = int(input("\nEnter your choice here: "))
        if choice==1:
            print("\t Payment Portal")
            print("\t Pick your convenient plan:")
            TotList = []
            Plan1 = ['1', "Basic Plan - INR 499", "1. Daily unlimited data (50 Mbps)\n2. Complimentary App(Amazon Kindle)","30 days","Yes"]
            Plan2 = ['2', "Super Combo - INR 799", "1. Daily unlimited data (75 Mbps)\n2. Free Disney + Hotstar VIP, \n3. Complimentary App(Amazon Kindle)", "30 days", "Yes"]
            Plan3 = ['3', "Family Pack - INR 1549\n(Top Grossing)", "1. Daily unlimited data (150 Mbps)\n2. Amazon Prime(Music, Shopping, Movies), \n3. Free Disney + Hotstar VIP, \n4. Complimentary App(Amazon Kindle)", "45 days", "Yes"]
            Plan4 = ['4', "Superlink Special - INR 2565\n(Limited Period Offer)", "1. Daily unlimited data (1 Gbps)\n2. Amazon Prime(Music, Shopping, Movies), \n3. All OTT Apps, \n4. Complimentary App(Amazon Kindle)", "60 days", "Yes"]
            TotList = [Plan1, Plan2, Plan3, Plan4]
            #tabulate module
            headers = ["SNo", "Plan & Price", "Benefits", "Validity", "Autopay available"]
            print(tabulate(TotList, headers, tablefmt="grid"))

            try:
                choice2 = int(input("\nEnter your choice here: "))
                #initializing date and time
                date = str(datetime.date.today())
                now = datetime.datetime.now()
                CTime = now.strftime("%H:%M:%S")
                
                if choice2==1:
                    print("You chose Basic Plan.")
                    time.sleep(2)
                    print("Payment is processing through your saved wallet.")
                    cursor.execute("INSERT INTO CONSUMERS_SUBSCRIPTIONS VALUES({},'{}', '{}', '{}', '{}', '{}')".format(subrows, cons[1], cons[6], Plan1[1], "1. Daily unlimited data (50 Mbps), 2. Complimentary App(Amazon Kindle)", date+", "+CTime))
                    conn.commit()
                    time.sleep(1)
                    print("Basic Plan - Payment successful. Thank you for using SuperLink. You will get all the beneficials soon!")
                    
                elif choice2==2:
                    print("You chose Super Combo Plan.")
                    time.sleep(2)
                    print("Payment is processing through your saved wallet.")
                    cursor.execute("INSERT INTO CONSUMERS_SUBSCRIPTIONS VALUES({},'{}', '{}', '{}', '{}', '{}')".format(subrows, cons[1], cons[6], Plan2[1], "1. Daily unlimited data (75 Mbps), 2. Free Disney + Hotstar VIP, 3. Complimentary App(Amazon Kindle)", date+", "+CTime))
                    conn.commit()
                    time.sleep(1)
                    print("Super Combo Plan - Payment successful. Thank you for using SuperLink. You will get all the beneficials soon!")
                
                elif choice2==3:
                    print("You chose Family Pack Plan.")
                    time.sleep(2)
                    print("Payment is processing through your saved wallet.")
                    cursor.execute("INSERT INTO CONSUMERS_SUBSCRIPTIONS VALUES({},'{}', '{}', '{}', '{}', '{}')".format(subrows, cons[1], cons[6], Plan3[1], "1. Daily unlimited data (150 Mbps), 2. Amazon Prime... Complimentary App(Amazon Kindle)", date+", "+CTime))
                    conn.commit()
                    time.sleep(1)
                    print("Family Pack Plan - Payment successful. Thank you for using SuperLink. You will get all the beneficials soon!")
                
                elif choice2==4:
                    print("You chose Superlink Special Plan.")
                    time.sleep(2)
                    print("Payment is processing through your saved wallet.")
                    cursor.execute("INSERT INTO CONSUMERS_SUBSCRIPTIONS VALUES({},'{}', '{}', '{}', '{}', '{}')".format(subrows, cons[1], cons[6], Plan4[1], "1. Daily unlimited data (1 Gbps), 2. Am... All OTT Apps, 4. Complimentary App(Amazon Kindle)", date+", "+CTime))
                    conn.commit()
                    time.sleep(1)
                    print("Superlink Special Plan - Payment successful. Thank you for using SuperLink. You will get all the beneficials soon!")
                
                else:
                    print("Invalid plan choice. Payment cancelled.")
            except ValueError and TypeError:
                print("Your given choice is invalid!")
        
        elif choice==2:
            cursor.execute("SELECT * FROM CONSUMERS_SUBSCRIPTIONS WHERE (Name='{}') &&MobileNo='{}'".format(cons[1], mobno))
            currentPlans = cursor.fetchall() #Fetch all plans of the user
            #Check and display user plans with conditions
            if totalplans==0:
                print("You currently don't have any subscriptions! Kindly recharge and check again")
            else:
                print(tabulate(currentPlans, header1, tablefmt="grid"))
        
        elif choice==3:
            if totalplans!=0:
                cursor.execute("SELECT * FROM CONSUMERS_SUBSCRIPTIONS WHERE (Name='{}') &&MobileNo='{}'".format(cons[1], mobno))
                currentPlans = cursor.fetchall() #Fetch all plans of the user

                print("\nYour Current Subscriptions:")
                print(tabulate(currentPlans, header1, tablefmt="grid"))
                print("Refer the above table and choose one of the available Options:")
                print("1. Revoke oldest and activate the queued subscription")
                print("2. Delete all subscriptions")
                print("0. Exit")

                try:
                    manage_sub_choice = int(input("Enter one of the following options to manage subscription: "))
                    if manage_sub_choice==1:
                        #Check whether they have queue plans or not with if and else
                        if totalplans>1:
                            print("Processing request...\n=====================")
                            time.sleep(3)

                            #1. Deleting old plan from database
                            cursor.execute("DELETE FROM CONSUMERS_SUBSCRIPTIONS WHERE (Recharge_id={}) &&MobileNo='{}'".format(topmostPlan[0],topmostPlan[2]))
                            conn.commit()
                            print("Recharge ID: ",topmostPlan[0],"\nPlan Name: ",topmostPlan[3],"\nBeneficials: ",topmostPlan[4],"\nRegistered Mobile No.: ",topmostPlan[2])
                            print("Has been successfully deleted and activated the queued plan!\n")

                            #2. Displaying next plan to be used from database
                            cursor.execute("SELECT * FROM CONSUMERS_SUBSCRIPTIONS WHERE MobileNo='{}'".format(mobno))
                            nextPlan = cursor.fetchone()
                            time.sleep(3)
                            print("\nACTIVATED PLAN: \nRecharge ID: ",nextPlan[0],"\nPlan Name: ",nextPlan[3],"\nBeneficials: ",nextPlan[4],"\nRegistered Mobile No.: ",nextPlan[2])
                        else:
                            print("You don't have any queue subscriptions to activate.")
                    elif manage_sub_choice==2:
                        confirmation = input("Are you sure you want to delete all subscriptions? (yes/no): ")
                        if confirmation.lower()=="yes":
                            #Checking whether user is having any plan or not
                            if totalplans>=1:
                                cursor.execute("DELETE FROM CONSUMERS_SUBSCRIPTIONS WHERE (Name='{}') &&MobileNo='{}'".format(topmostPlan[1],topmostPlan[2]))
                                conn.commit()
                                print("You had ",totalplans, "and they are deleted successfully!")
                            else:
                                print("You don't have any queue subscriptions to activate.")
                        else:
                            print("Process canceled!")
                            exit()
                except ValueError and TypeError:
                    print("Your given choice is invalid!")
            else:
                print("You don't have any plans to manage subsriptions!")
                time.sleep(3)
                quit()

        elif choice==4:
            query = input("Welcome to support ticket!\n\nEnter your query to send:")

            date = str(datetime.date.today())
            now = datetime.datetime.now()
            CTime = now.strftime("%H:%M:%S")
            cursor.execute("INSERT INTO CONSUMERS_SUPPORT VALUES({},'{}', '{}', '{}','{}','{}')".format(sptrows, cons[1], cons[4], cons[6], date+", "+CTime,query))
            conn.commit()
            print("Sending...")
            time.sleep(3)
            print("We have received your query. We will sort it out and reach you soon. Thank you!")
        elif choice==0:
            quit()
    except ValueError and TypeError:
        print("Your given choice is invalid!")



else:
    print("Error. Check your login details and try again!")


conn.close()

if conn.is_closed():
    print("Connection successfully closed!")
