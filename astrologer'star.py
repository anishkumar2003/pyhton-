x=int(input("enter how many lines of star you want to print:"))
a=int(input("chose one of the number(0,1):"))
if(a==1):
    for i in range(0,x):
            for j in range(0,i+1):{
                print("*",end="")}
            print("\n")                                  
else:
    for i in range(1,x):
        for j in range(0,x-i):{#use 188 a specific pattren
            print("*",end="")}
        print("\n")
