
count=dict()
fname=open(input('Enter File Name: '))
for line in fname:
    if not line.startswith('From: '):continue
    word=line.split()
    words=word[1]
    count[words]=count.get(words,0)+1

largest=-1
email=None
for k,v in count.items():
    if v>largest:
        largest=v
        email=words
print('Maximum email sender is',email,'with',largest,'Nos of emails')
