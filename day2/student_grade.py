name = input("enter student name:")
cls = input("enter class:")

m1=int(input("enter marks of subject 1:"))
m2=int(input("enter marks of subject 2:"))
m3=int(input("enter marks of subject 3:"))
m4=int(input("enter marks of subject 4:"))
m5=int(input("enter marks of subject 5:"))

total = m1+m2+m3+m4+m5
per = total / 5

    
if per>60:
    
    print("grade A")

elif per>50:
    
    print("Grade B")
elif per>40:
    print("Grade c")
else:
    print("fail")

print("name=",name)
print("total=",total)
print("class=",cls)
print("percentage=",per)