balance = float(raw_input('Enter the outstanding balance on your credit card:  '))
intrest = float(raw_input('Enter the annual credit card interest rate as a decimal:  '))
rate = float(raw_input('Enter the minimum monthly payment rate as a decimal:  '))
total_amount_paid=0.0
for i in range(1,13):
    print 'Month:',i
    total_amount_paid=0
    Min_month_payment=rate*balance
    intrest_paid=((intrest)/(12))*balance
 
    principle_paid=Min_month_payment-intrest_paid
    balance_remaining=balance-principle_paid
    
    print 'Minimum monthly payment:$',Min_month_payment
    print 'Principle paid:$',principle_paid
    print 'Remaining balance:$',balance_remaining
    balance=balance_remaining
    total_amount_paid=total_amount_paid+principle_paid

print 'RESULT'
print 'Total amount paid:$',total_amount_paid
print 'Remaining balance:$',balance_remaining
