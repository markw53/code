import math
width = float(input('Enter the width in metres: '))
length = float(input('Enter the length in metres: '))
height = float(input('Enter the height in metres: '))
if width > 0 and length > 0 and height > 0:
    decor = input("Type 'w' for wallpaper of 'p' for paint: ")
    if decor == 'W' or decor == 'w':
        area = 2 * ((width * height) + (length * height))
        roll = 0.6 * 10
        totalrolls = math.ceil(area / roll)
        print (f'You need {totalrolls} roll(s)')
    elif decor == 'P' or decor == 'p':
        area = 2 * ((width * height) + (length * height))
        tins = math.ceil(area / 20)
        print (f'You need {tins} tin(s) of paint')
    else:
        print('Wrong decor type!')
else:
    print('Incorrect measurement!')

