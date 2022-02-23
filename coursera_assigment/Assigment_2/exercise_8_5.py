fname=open(input('Enter File Name: '))
count=0
for line in fname:
    if not line.startswith('From: '):continue
    word=line.split()
    print(word)
    count=count+1
print("There were", count, "lines in the file with From as the first word")
