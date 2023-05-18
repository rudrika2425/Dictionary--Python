d1={'key1': 1, 'key2': 3, 'key3': 2}
d2={'key1': 1, 'key2': 2}
flag=0
for a,b in d1.items():
    for c,d in d2.items():
        if(a==c and b==d):
            print(a,b,"are equal")
            flag=1
            break
if flag==0:
    print("none")        
        
              