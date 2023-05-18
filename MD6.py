n=int(input())
s=[]
for k in range(1,n+1):
    s.append(k)
print(s)
d={i:int(i)*int(i)for i in s}
print(d)
