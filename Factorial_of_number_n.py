n = int(input("Enter the number to calculate Factorial: "))
if(n < 0 ):
    print("Negative numbers are not allowed")
elif(n == 0 or n == 1):
    print("Fact = 1")
else:
    Fact = 1
    i = 2
    while (i <= n):
        Fact = Fact * i
        i = i + 1
    print(Fact)