hours=float(input('Enter hours of works: '))
rate=float(input('Enter rate per hours: '))
def computepay(h,r):
    if h>=40:
        gross_pay=40*r+(h-40)*r*1.5
    else:
        gross_pay=h*r

    return gross_pay

print('Your Pay Rate is',computepay(hours,rate))
