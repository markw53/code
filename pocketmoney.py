pocketMoney = 0.01
totalMoney = 0
for week in range(64):
    print("\nIt is week ",week)
    print("You will get £",pocketMoney)
    pocketMoney = pocketMoney * 2
    totalMoney = totalMoney + pocketMoney
print("You have £",totalMoney)
input("\nPress ENTER to exit program")

