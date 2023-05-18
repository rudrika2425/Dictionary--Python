s=0
d1={'key1': 1, 'key2': 3, 'key3': 2}
ls=list(d1.values())
for i in ls:
    s+=i
ls2=list(d1.keys())
dct={}.fromkeys(ls2,s)
print(dct)