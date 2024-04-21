import math
fueltype = input("What fuel do you use? \n Enter 'P' for petrol, 'D' for diesel or 'L' for LPG ")
amount = float(input("How much have you put in in Litres? "))
if fueltype == 'p' or fueltype == 'P':
    totalprice = amount * 1.49
elif fueltype == 'd' or fueltype == 'D':
    totalprice = amount * 1.69
else:
    totalprice = amount * 0.95
paid = float(input("How much did you hand over? £"))
change = round(paid - totalprice,2)
print(f"You have £{change} change")
loyalty = input("Do you have a loyalty card, (y)es or (n)o? ")
if loyalty == 'Y' or loyalty == 'y':
    points = math.floor(amount) + math.floor(totalprice)
    if points > 100:
        points = points * 1.1
        total = math.floor(points)
        print (f"You have earned {total} loyalty points")
    else:
        print (f"You have earned {points} loyalty points")
else:
    print("Maybe you should apply for a card.")

    