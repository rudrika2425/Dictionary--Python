d={"1":"2","3":"4","5":"6","7":"8","7":"9"}
re=[]
for keys in d:
    if keys not in re:
        re+=keys
    else:
        d.pop(key)   
print(d)         
        