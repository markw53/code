# This line prints Hello World!
print ("Hello, World!")

# Function to calculate simple interest
def SI():
    P = 1500000
    R = 0.05
    T = 5
    SimpleInt = P*R*T
    print(SimpleInt)
    
SI()

# Prints a blank line
print()

# Function to calculate the area of a rectangle
# def areaRectangle():
#    length = 10
#    breadth = 5
#    area = length * breadth
#    print (area)
#    if a == b:
#        print(a)

# areaRectangle()

# Python Indentation
ab = 5
bc = 5
if ab == bc:
    print("Both numbers are 5")
    print("Welcome")
    print("bye")
    
myPhoneNumber = 80 # camelCase
MyPhoneNumber = 80 # PascalCase
my_phone_number = 80 # snake_case
myphonenumber = 1

print (myphonenumber)

my_Name = "Timothy"
print(my_Name)

first_name = "Bob"
school_attended = "Eton"
my_age = 21
last_name = "Simpson"

type(first_name)

# Write a code that finds the simple interest of a sum given the principal as 1500000, rate is 5% and time is 3 years
def Simple_Interest():
    p = 1500000
    r = 0.05
    t = 3
    Simple_Int = p*r*t
    print(Simple_Int)
    
Simple_Interest()

# This calculates the simple interest using inputs
def calculate_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate as a percentage: "))
    rate = rate/100
    time = int(input("Enter the number of years: "))
    interest = principal * rate * time
    print (f"You are owed £{interest}")
               
calculate_interest()

# Sum of three inputted values
def addition():
    Cole = float(input("Cole, please enter your amount: £"))
    Nicole = float(input("Nicole please enter your amount: £"))
    Derek = float(input("Derek please enter your amount: £"))
    total = Cole + Nicole + Derek
    print (f"You have a total of £{total} between you")
    
addition()
