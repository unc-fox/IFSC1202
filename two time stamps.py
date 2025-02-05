print ("first time stamp")
h1= int(input("Hours:" ))
m1= int(input("minutes:" ))   
s1= int(input("seconds:" ))

print ("second time stamp")
h2= int(input("Hours:" ))
m2= int(input("minutes:" ))
s2= int(input("seconds:" ))

t1= h1*3600 + m1*60 +s1
t2= h2*3600 + m2*60 +s2
diff = t2-t1
print (diff)