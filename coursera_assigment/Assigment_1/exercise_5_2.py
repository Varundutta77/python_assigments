smallest=None
largest=0

while True:
    number=input('Enter Number: ')
    if number=='Done' or number=='done':
        break
    try:
        num=float(number)
    except:
        print('Enter correct input: ')
        continue

    if smallest is None:
        smallest=num
    if smallest > num:
        smallest=num
    if largest < num:
        largest=num

print('Largest number is: ',largest)
print('Smallest number is: ',smallest)
