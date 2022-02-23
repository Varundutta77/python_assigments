fname = open(input("Enter file name: "))
count = 0
ftotal = 0
for line in fname:
    if not line.startswith("X-DSPAM-Confidence:"):continue
    ffloat = float(line[19: ])
    ftotal = ftotal + ffloat
    count = count + 1

print('Average spam confidence:', ftotal/count)
