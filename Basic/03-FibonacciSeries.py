def FibonacciSeries(intHowMany):
    '''
This is my first Python Function. 
This function returns the Fibonacci series taking "n" as an arugumet,
which is the number of Fibonacci numbers to print
    '''

    intCurrentValue = 0
    intNextValue = 1

    intCounter = 1
    while intCounter <= intHowMany:
        if intCounter == 1:
            intFibonacciNumber = 1 
            print("Fibonacci Series [%s] is %s" % (intCounter, intFibonacciNumber))
            intCounter = intCounter + 1
        else:
            intFibonacciNumber = intCurrentValue + intNextValue 
            print("Fibonacci Series [%s] is %s" % (intCounter, intFibonacciNumber))
            intCurrentValue, intNextValue, intCounter = intNextValue, intFibonacciNumber, intCounter + 1
    return

print(FibonacciSeries.__doc__)
intHowMany = input("\nHow many number in the Fibonacci series do you want? ")
FibonacciSeries(int(intHowMany))

