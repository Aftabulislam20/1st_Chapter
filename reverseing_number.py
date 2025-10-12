#sum of the given numbers
Number = list(input("Enter your number: "))
Number.reverse()
final = "".join(str(i) for i in Number)
print(final)