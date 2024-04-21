text = input('Please enter some text \n')
text = (len(text) == 1)
if text.strip().isdigit():
   print ('You entered a number')
else:
   print ('You entered a string')


