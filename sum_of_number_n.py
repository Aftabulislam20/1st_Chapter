# প্রথম n সংখ্যার যোগফল
n = int(input("Enter the number to calculate the first n number sum: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i += 1
print(sum)