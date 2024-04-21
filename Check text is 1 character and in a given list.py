choices = ['A', 'B', 'C', 'D', 'E', 'F', 'T', 'V', 'W', 'X', 'Y', 'Z']
text = input('Please enter some text: \n')
if (len (text) == 1 and text.isalpha() == True and text in choices):
    print ('Perfect!')
else:
    print ('Whoops!')

    



