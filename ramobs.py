n=int(input("enter some value"))for i in range(n):    for j in range(i+1):        print("*",end=" ")    for j in range(n):        print(" ",end=" ")        for j in range(n-i-1):            print("*",end=" ")    print( )