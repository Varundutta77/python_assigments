fname=open(input('Enter File Name: '))
fread=fname.read()
fsplit=fread.split()
data=[]
for line in fsplit:
    if line not in data:
        data.append(line)
print(sorted(data))
