from array import *

a1 = array('i',[12,45,76,78])
print(type(a1))
print(a1)
for x in a1:
    print(x)

for i in range(4):
    if a1[i] > 50:
        print(a1[i]) 
    else:
        print(a1[i],"less than 50")

i= 0
while (i <len(a1)):
    print(a1[i])
    i+=1

a1.append(59)
print(a1)
print(a1.count(34))
print(a1.count(45))

print(a1.index(45))

print(a1.pop(0))

str = "JAI shree ram"
print(str.lower())
