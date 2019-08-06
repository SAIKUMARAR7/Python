dict1={'a1':100,'a2':24,'a3':56}
dict2={'a1':26,'a3':44,'a5':78}
for key in dict1:
    if key in dict2:
        dict1[key]=dict1[key]+dict2[key]
    else:
        continue
print(dict1)   
