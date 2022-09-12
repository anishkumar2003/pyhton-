x=45 # here x is a golbal variable
def anish():
    x=46
    print(x)# it print 46 because it is a local variable.
anish()
print(x)#45 is printed because it is out of anish function.
def dishu():
    global x#here global is keyword use to change the value of global variable.
    x=39
    print(x)
dishu()
print(x)# here value of x=39 is printed because a keyword global is used which change the value of global varialble.
