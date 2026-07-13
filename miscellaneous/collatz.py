def collatz():
    print ('pick a number')
    number = int(input())
    while number > 1:
        print "your number is now " + str(number)
        if (number % 2)==0:
            number1 = number // 2
            print (str(number) + " // 2 = " + str(number1))
            number = number1
        else:
            number2 = 3 * number + 1
            print ("3 * " + str(number) + " + 1 = " + str(number2))
            number = number2
    print "your number is now " + str(number)
collatz()
