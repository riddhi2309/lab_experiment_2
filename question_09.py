monthly_installment = float(input("Enter the value of the monthly installment(min= 500):-"))
duration = int(input("enter the durationof the installment(min=6):-"))
intrest = 7.1/100
total_amount = 0
for i in range(duration):
    monthly_intrest = (monthly_installment + total_amount)*intrest/12
    total_amount += monthly_installment + monthly_intrest
print(f"total amount after{duration} months: Rs {total_amount:.2f}")