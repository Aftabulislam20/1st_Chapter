#sum of the given numbers
Number = list(input("Enter your number"))
print(type(Number))
Number.reverse()
final = "".join(str(i) for i in Number)
print(final)