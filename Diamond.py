n = int(input("Enter number of rows: "))
[print(''* abs(n-i) + '*' * (2 * (n-abs(n-i))-1)) for i in range(1,2*n)]


