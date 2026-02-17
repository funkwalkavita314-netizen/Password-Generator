import random
import string

print("======PASSWORD GENERATOR=====")

while True:
    try:
        length=int(input("enter length of passwd"))
        if length<=0:
            print("please enter positive length")
            continue

        print('''/n enter password type
1. only letters
2. letters + numbers
3. letters + numbers + special characters''')

        choice=input("enter choice (1-3)")

        if choice=="1":
            char=string.ascii_letters

        elif choice=="2":
            char=string.ascii_letters + string.digits

        elif choice=="3":
            char=string.ascii_letters + string.digits + string.punctuation

        else:
            print("invalid choice")
            continue

        password="".join(random.choice(char) for _ in range(length))

        print("Password Generated:",password)

    except ValueError:
        print("please enter a valid number!")



    again=input("/n Generate another password? (yes/no):").lower()
    if again!="yes":
        print("Thankyou for using password generetor")
        break
    
