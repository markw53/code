def calculate_interest():
    principal = float(input("Enter the principal amount: "))
    years = float(input("Enter the number of years: "))
    if years <= 3:
        rate = 0.03
    elif years >7:
        rate = 0.06
    else:
        rate = 0.05
    interest = principal * rate * years
    print (f"You are owed £{interest}")
               
calculate_interest()
