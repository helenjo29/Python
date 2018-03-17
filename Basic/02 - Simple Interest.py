intPrincipal = input("\nEnter Principal: ")
intNumberOfYears = input("Enter Number of Years: ")
floatRateOfInterest = input("Enter Rate of Interest: ")

floatSimpleInterest = (int(intPrincipal) * int(intNumberOfYears) * float(floatRateOfInterest))/100
print ("Simple Interest is: %0.2f" %floatSimpleInterest)