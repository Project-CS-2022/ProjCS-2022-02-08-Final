from superlink import security
import mysql.connector as sqltor
import datetime #Library
import requests #fetch module
import time

security.security_init()
secure = security.isSecured()

#main
if secure == True:

    conn = sqltor.connect(host="localhost", user="root", passwd="root", database="sadn")
    cursor = conn.cursor()

    if conn.is_connected():
        print("Successfully connected!")
    
    #Creating Table
    cursor.execute("CREATE TABLE IF NOT EXISTS Crypto(SNo integer(2),Price varchar(20),Time varchar(10))")#.format(TodayDate = datetime.date.today())

    #creating function to avoid complications
    def crypto():
            apiKey = 'sk_032bd526e86f4e4dbceab0f7e48fe134'
            api_url = f'https://cloud.iexapis.com/stable/crypto/btcusd/price?token={apiKey}'
            req = requests.get(api_url).json()
            price = req['price']  #indexing dictionary from API
            return float(price)*75  #conversion

    for i in range(1, 16):
        now = datetime.datetime.now()
        CTime = now.strftime("%H:%M:%S")
        Crypto = crypto()
        cursor.execute("INSERT INTO Crypto VALUES({},{},'{}')".format(i,Crypto,CTime))
        conn.commit()
        print('Price lookup {}: {} INR'.format(i,Crypto))
        time.sleep(20)

    print("Data successfully recorded to the database!")

    #Closing the connection
    conn.close()

    if conn.is_closed():
        print("Connection successfully closed!")