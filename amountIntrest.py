#  the deposite amount by billy
amount_deposite=1000
# the rate of intrest
intrest_rate=5
#the time period 
time=10
#calculating the simple intrest
simpleintrest=amount_deposite*intrest_rate*time//100
#total amount after adding the intrest
amount=amount_deposite+simpleintrest
#result variable for displaying amount upto 2 decimal places
result = "{:,.2f}".format(amount)
print("Bill’s total wealth is $",result)

