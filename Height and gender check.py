male = ['Male','male','M','m']
female = ['Female','female','F','f']
height = input ('What is your height in cm? ')
height = float(height)
gender = input('What is your gender? ')
if height > 150 and height < 190 and gender in male:
    print ('You are of average height.')
elif height > 130 and height < 170 and gender in female:
    print ('You are of average height.')
else:
    print ('You are not average!')
