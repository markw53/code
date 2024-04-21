def check_user_input(input):
    try:
        # convert into an integer
        val = int(input)
        print ('Input is an integer number. Number = ',val)
    except ValueError:
        try:
            #convert into a float
            val = float(input)
            print ('Input is a float number. Number = ',val)
        except ValueError:
            print ("No..input is not a number. It's a string")

input1 = input('Enter some text: ')
check_user_input (input1)

