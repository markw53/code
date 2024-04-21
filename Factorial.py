import math

number = int(input("Enter a number: "))
if number == 0:
    print(f"The factorial of {number} is 0")

else:
    result = 1
    for i in range(1,number):
        result += result * i

    print(f"The factorial of {number} is {result}")
      


