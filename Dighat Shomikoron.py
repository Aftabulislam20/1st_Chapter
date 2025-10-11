#দিঘাত সমীকরন
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
D = (b*b) - (4*a*c)
if(D > 0):
    x1 = (-b + D**0.5)/ 2*a
    x2 = (-b - D**0.5)/ 2*a
    print(x1, x2)
elif(D == 0):
    x = -b / (2*a)
    print(x)
else:
    print("Roots are imaginery..")