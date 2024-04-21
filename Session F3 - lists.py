myList = [] # this is an empty list
list1 = [1,2,3,0,"Julius",True]
myFruit = ["Apple", "Orange", "Grapes", "Mango", "Pineapple", "Banana"]

print(myFruit[:3])

myBasket = ["Apple", "Orange", "Grapes", "Mango", "Pineapple", "Banana"]

print(myBasket)

subFruit = myBasket[3:6] # creates a new list from an original
print(subFruit)

print(len(myBasket)) # prints how many items are in the list

myBasket.append("Guava") # adds a new item to a list

print(myBasket) # outputs the appended list

myBasket.append("Sugarcane")
myBasket.append("Watermelon")

print(myBasket)

myBasket.extend(["Cherries", "Kiwi", "Lemon", "Peach"])

print(myBasket)

myBasket.pop(0)
print(myBasket)

myBasket.remove("Sugarcane")
print(myBasket)

print(myFruit)
myFruit[5] = "Guava" # replace a specific item
print(myFruit)

myFruit.sort()
print(myFruit)

myFruit.sort(reverse = True)
print(myFruit)

NewFruitBasket = myFruit.copy()
NewFruitBasket.append("Strawberry")
print(NewFruitBasket)
print(myFruit)
