# Sum of two numbers
a = 5   # Taking input of a
b = 10  # Taking input of b
sum = a + b # Calculating
print(sum)  # printing output

# Are of rectangle
length = 20 # taking input of length
width = 30  # taking input of width
rectangle_area = length * width   # Calculating
print(rectangle_area) # printing output in terminal

# area of right angle
base = 30   # taking input of base
height = 20 # taking input of height
right_angle_area = int(1/2 * base * height)  # calculating
print(right_angle_area) # displaying on terminal

# area of circle
radius = input("Enter the circle radius: ")  # taking input of r radius
pi = 3.1416 # giving input of pi
area_of_circle = pi * radius * radius   # #calculating are of circle
print(area_of_circle)   # giving result in terminal

# tranfer farenheight temparature to centigrade temparature
farenheight = 54    # taking input of farenheight
celcius = (farenheight - 32) * 5/9  # converting to celcius
print(celcius)  # printing output in terminal

# check which number is largest among 3 numbers
a = 50  # taking first number
b = 100 # taking 2nd number
c = 60  # taking 3rd number
if(a < c and b < c):    # checking
    print("c is largest")
elif(a < b and c < b):  # 1st check was wrong trying for 2nd
    print("b is largest")
else:                   # all was wrong this is right
    print("a is largest")

# printing are of any triangle 
base_1 = int(input("Enter the base 1 value")) # all 3 base input
base_2 = int(input("Enter the base 1 value"))
base_3 = int(input("Enter the base 1 value"))
if(base_1 + base_2 > base_3 and base_2 + base_3 > base_1 and base_1 + base_3 > base_2): # checking of horon's formula requirements
    s = (base_1 + base_2 + base_3) / 2
    area_square = s * (s - base_1) * (s - base_2) * (s - base_3)    # calculating without root
    area = area_square ** 0.5   # with root
    print(area) # printing area in terminal
else:
    "Calcuulation not possible"
# দিঘাত সমীকরন এর মুল
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
D = (b*b) - (4*a*c)
if(  D > 0 ):
    x1 = (-b + (D ** 0.5)) / (2 * a)
    x2 = (-b - (D ** 0.5)) / (2 * a)
    print(x1, x2)
else:
    if( D == 0 ):
        x = -b / (2 * a)
        print(x)
    else:
        print("Roots are imaginary")
# factorial of first n number
n = int(input("Enter the last number: "))
if( n < 0):
    print("Negative numbers are not allowed")
elif( n==0 or n==1):
    print("Fact = 1")
else:
    i = 2
    Fact = 1
    while(i <= n):
        Fact = Fact * i
        i = i + 1
    print(Fact)

# sum of first n numberr
n = int(input("Enter the last number: "))
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1
print(sum)





