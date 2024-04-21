pocketMoney = 0.01
totalMoney = 0
for week in range(26):
    print("\nIt is week ",week)
    print(f"You will get £{pocketMoney}")
    pocketMoney = pocketMoney * 2
    totalMoney = totalMoney + pocketMoney
print(f"You have £{totalMoney}")
input("\nPress ENTER to exit program")

                
