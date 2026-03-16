import hashlib
import re
dict = {}

def haspassword(passwd):
    return hashlib.sha256(passwd.encode()).hexdigest()

def validatepasswd(password):
    if len(password)<8:
        return False
    elif not re.search(r"[A-Z]",password):
        return False
    elif not re.search(r"[a-z]",password):
        return False
    elif not re.search(r"[0-9]",password):
        return False
    elif not re.search(r"[@$!%*?&]",password):
        return False
    else:
        return True

def createuser():
    usr = input("Create your username\n")
    passwd = input("Create your password\n")
    if validatepasswd(passwd):
        print("Password is valid\n")
        stored_passwd = haspassword(passwd)
        dict[usr] = stored_passwd
    else:
        print("Password is not valid\n")
        exit()


while(True):
    print('''
    1.Create a new user
    2.Login as a user
          ''')
    choice = int(input("Enter your choice\n"))
    if choice == 1:
        createuser()
    elif choice == 2:
        usr = input("Enter your username\n")
        if usr in dict:
            passwd = input("Enter your password\n")
            if dict[usr] == haspassword(passwd):
                print("You have successfully logged in\n")
                exit()
            else:
                print("Wrong password")
                exit()
        else:
            print("User does not exist\n")
            exit()


