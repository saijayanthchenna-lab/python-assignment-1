principle=float(input("Enter the principle amount:" ))
rate=float(input("Enter the rate of interest: "))
time=float(input("Enter the time of interest: "))
amount=principle*(1+rate/100) ** time
print("the amount is",round(amount,2))
ci=amount-principle
print("The compound amount is",round(ci,2))