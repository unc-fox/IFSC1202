x = int (input("Enter Maximum Height: "))
for i in range(1,x+1): #this is giving me the count value from 1 to "x"
    print ("*" * i) # this is what confused me before. the print statement is multiplying the * by the count, not the value of x
for i in range (x -1,0,-1): # this is the descending portion. X is still my maximum height, the first -1 is showing the first count decreasing. the 0 is the lowest range and the second -1 is the increment 
    print ("*" *i)