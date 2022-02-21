hours=float(input('Enter No. of Hours of Works : '))
rate=float(input('Enter Rate per Hours: '))
if hours<40:
    pay=rate*hours
if hours>=40:
    pay=40*rate+((hours-40)*1.5*rate)

print('Your Pay rate is : ',float(pay))
