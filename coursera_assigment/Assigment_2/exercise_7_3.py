fname=open(input('Enter File Name : '))
fread=fname.read()
fsplit=fread.split()
data=[]
for word in fsplit:
        if word not in data:
            data.append(word)
print(sorted(data))
