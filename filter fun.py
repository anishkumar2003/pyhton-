list1=[1,2,3,4,5,6,7,8,9,10,12,16]
def greater(n):
    return n>5
ls=list(filter(greater,list1))
print(ls)
def lesser(n):
    return n<8
ls2=list(filter(lesser,list1))
print(ls2)
def in_range(n):
    return n in range(4,9)
ls3=list(filter(in_range,list1))
print(ls3)
def perfect_square(n):
    if (n**0.5)%1==0:
        return n
    else:
        pass
ls4=list(filter(perfect_square,list1))
print(ls4)
