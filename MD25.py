d={}
for i in range(0,3):
    for j in range(0,3):
        d[i,j]=input()
        
print(" NAME ", " AGE ", "  COURSE ")
for i in range(3):
    for j in range(3):
        print(d[(i, j)], end='   ')
 
    print()        