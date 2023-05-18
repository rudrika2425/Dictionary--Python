d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
ls=list(d.values())
ls.sort()
a=ls[-1]
b=ls[-2]
c=ls[-3]
print(a)
print(d.key[a])
