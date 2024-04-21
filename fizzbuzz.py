def fizzbuzz(number):
    for num in range (1,number):
        if num % 15 == 0:
            print ("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print (num)

number = int(input("Enter a number: "))

fizzbuzz(number)


