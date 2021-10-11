#the deposite amount by Billy
saving_amount_deposite=5000
#time period to double the amount
time_period=6
#intrest rate
rate_of_intrest=20
#calculating simple intrest
simple_intrest=saving_amount_deposite*time_period*rate_of_intrest//100
#if the value of simple intrest is >= saving amount deposite 
#then print true else print false
if(simple_intrest>=saving_amount_deposite):
    print("True")
else:
    print("False")