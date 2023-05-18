d={'a':200,'b':300,'c':100}
list=[]
s=1
for i in d:
    list.append(d[i])
for j in list:
    s*=j
print(s)    