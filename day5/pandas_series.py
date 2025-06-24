import pandas as pd

#pandas series from dictionary
dict={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
s = pd.Series(dict)
print(s)

#pandas series from list
list=[10,20,30,40,50]
s2 = pd.Series(list)
print(s2)


#access the elements of a series in pandas

print("\nindex:",s[0])  
print("\nlable:",s['a']) 
print("\nslicing:  ",s[1:3])  





