dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
c=dic1|dic2|dic3
print(c)
dic2.update(dic1)
print(dic2)
