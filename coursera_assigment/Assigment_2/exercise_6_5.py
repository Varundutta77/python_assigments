text = 'X-DSPAM-Confidence:    0.8475'
ipos=text.find('0')
pos=text[ipos:]
print(pos)
number=float(pos)
print(number)
