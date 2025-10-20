#বইয়ের নিয়ম অনুসারে যেকোন ‍ত্রিভুজের ক্ষেত্রফল বের কর
import math
a = float(input("Enter the first base value: "))
b = float(input("Enter the second base value: "))
c = float(input("Enter the third base value: "))
if( a + b > c and b + c > a and c + a > b):
    s = (a + b + c) / 2
    area = math.sqrt(s*(s - a)*(s - b)*(s -c))
    print("Triangle area is=",area)
else:
    print("Triangle is not possible")