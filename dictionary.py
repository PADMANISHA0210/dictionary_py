# DICT UNORDERED MUTABLE DOESN'T ALLOWS DUPLICATE
d={'n':'NISHA',1:'PYTHON'}
#traversing
for i in d:
    print(i)
for i in d:
    print(i,d[i]) 
#mutable   
d[1]='LUCKy'
print(d)   
#add
d['s']='KUTTI'
print(d)
#remove
d.pop(1)
print(d)
#update(like extend in  list)
e={'1':'college','2':'job'}
d.update(e)
print(d)
#to print keys
print(d.keys())
#to print values
print(d.values())
print('NISHA' in d) #only keys can be checked