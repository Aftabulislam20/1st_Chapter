def plus():
    print(a + b)
def minus():
    print(a - b)
def multi():
    print(a * b)
def division():
    print(a / b)   

print("Choose a option with the serial: ")
print("1. +\n2. -\n3. *\n4. /\n5. quit")
user_choice = input("Choose a option :")
if(user_choice == "5"):
    print("Calculation ended...") 
elif(user_choice == "1"):
    a = int(input("Enter a number : "))
    b = int(input("Enter a Number : "))
    plus()
elif(user_choice == "2"):
    a = int(input("Enter a number : "))
    b = int(input("Enter a Number : "))
    minus()
elif(user_choice == "3"):
    a = int(input("Enter a number : "))
    b = int(input("Enter a Number : "))
    multi()
elif(user_choice == "4"):
    a = int(input("Enter a number : "))
    b = int(input("Enter a Number : "))
    division()
else:
    print("Symbol not defined...")

    
