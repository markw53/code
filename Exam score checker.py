score = input('What was your test score? ')
score = int(score)
if score > 90 and score <=100:
    print ('A*')
elif score > 80 and score < 90:
    print ('A')
elif score > 70 and score < 80:
    print ('B')
elif score > 60 and score < 70:
    print ('C')
elif score > 50 and score < 60:
    print ('D')
elif score > 40 and score < 50:
    print ('E')
elif score > 30 and score < 40:
    print ('F')
elif score >=0 and score < 30:
    print ('U')
else:
    print ('That can not be right!')

    



