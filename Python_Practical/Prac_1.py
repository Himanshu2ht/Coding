import math
def findRoot(a,b,c):
    D= math.sqrt(b**2 - 4*a*c)

    if(D>0):
        root1= (-b+D)/2*a
        root2= (-b-D)/2*a
        print("Roots are real and distinct, they are: ", root1, root2)
    
    elif(D==0):
        root= (-b+D)/2*a
        print("Roots are real and equal, they are: ", root, root)

    else:
        print("The roots are not real")

findRoot(1,-6,9)