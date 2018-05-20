# This purpose of this program is to find all the factors of an input
number = int(input("Please enter a positive integer: "))

factors = []
counter = 1
while counter < number:
    if number % counter == 0:
        factors.append(counter)
        print(counter, "is a factor of", number)
    else:
        print(counter, "is not a factor of", number)
    counter += 1

print("The factors of", number, "are:")
print(factors)