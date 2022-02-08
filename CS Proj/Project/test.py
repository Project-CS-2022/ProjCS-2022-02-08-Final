from superlink import security

security.security_init()


security = security.isSecured()
print(security)
if security==True:
    print("hellllllllo")
elif security=="locked":
    print("locked")
elif security==False:
    print("False!")


'''while security==True:
    print("Security=",security)
    security="Finished"
'''
#print(user.name(), user.gender(), user.location(), user.country(), user.mobileNo(), user.email(), user.registeredOn())

'''
import pickle
print("!!!WECOME TO PASSWORD CONFIG MANAGER!!!\nPassword must be:\n1. Alphanumeric\n2. Must be in 8 or more characters")
print("WARNING: Please store the password in safe place. This might be helpful in future incase if you forget it!\n\n")

passwd = input("Enter the strong password for the admin panel:")


if len(passwd)<=7:
    print("[ERROR] Password length must be 8 characters or more")
elif passwd.isalpha() == True:
    print("[ERROR] Password must be Alphanumeric")
elif passwd.isalpha() != True and len(passwd)>=8:
    with open("password.dat","wb") as f:
        pickle.dump(passwd,f)
        print("Password saved successfully in a binary file for safety purpose!")
else:
    print("Your password does not satisfy the requirements! Please run the configuration again.")
'''