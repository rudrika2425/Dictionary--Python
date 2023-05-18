ls=["hello","my","name"," is","rudrika"]
d={}
ls.sort()
for i in range(1,len(ls)+1):
    d[i]=ls[i-1]
print(d)