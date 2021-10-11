#the deposite amount by billy
amount_deposite=1000
#u the rate of intrest
intrest_rate=5
#the time period 
time=10
#Bill money double=amount deposite
double=amount_deposite
#calculating the simple intrest
simpleintrest=amount_deposite*intrest_rate*time//100
#Time T taken to double is
T=time*double//simpleintrest
timeperiod = "{:,.2f}".format(T)
print("It takes ",timeperiod,''' years to double Bill’s money.''')

      