t=tuple()
n=int(input ("total number of value in tuple"))
for i in range (n):
    a=input ("enter element")
    t=t+(a,)
print ("maximum value =",max (t))
print ("minimum value =",min (t))
print ("tuple is",t)
print ("tuple is", t)
x=t.count(4)
print ("4 in tuple",x)
