fname=input('Enter file Name: ')
f=open(fname)
count=dict()
for line in f:
    if line.find('From '):continue
    line=line.split()
    line=line[5]
    line=line.split(':')
    line=line[0]
    count[line] =  count.get(line, 0) + 1
count=sorted(count.items())
for hours,times in count:
    print(hours,times)
