import mysql.connector as sqltor
from superlink import security

security.security_init()
secure = security.isSecured()


if secure==True:
    print("Decrypted")
elif secure==False:
    print("False")
else:
    print("Locked")