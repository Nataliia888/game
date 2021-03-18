userName = input("Please enter your name: ")
print(userName.capitalize())
passwd = input("Please enter password: 1 upper case, 1 lower case, 1 numeric character [0-9]")
val = False

if len(passwd) < 6:
    print('length should be at least 6')
    val = False

if len(passwd) > 40:
    print('length should be not be greater than 9')
    val = False

if not any(item.isdigit() for item in passwd):
    print('Password should have at least one numeral')
    val = False

if not any(item.isupper() for item in passwd):
    print('Password should have at least one uppercase letter')
    val = False

if not any(item.islower() for item in passwd):
    print('Password should have at least one lowercase letter')
val = False
passwd = input("Please enter a new password")

if len(passwd) < 6:
    print('length should be at least 6')
    val = False

if len(passwd) > 40:
    print('length should be not be greater than 9')
    val = False

if not any(item.isdigit() for item in passwd):
    print('Password should have at least one numeral')
    val = False

if not any(item.isupper() for item in passwd):
    print('Password should have at least one uppercase letter')
    val = False

if not any(item.islower() for item in passwd):
    print('Password should have at least one lowercase letter')
if True:
    print("You successfully added the password")
if False:
    print("Sorry, try again in 24 hours")

