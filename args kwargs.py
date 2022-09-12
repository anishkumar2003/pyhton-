def fun(a,*b,**c):
    print(a)
    for item in b:
        print(item)
    print("\n")
    for key,value in c.items():
        print(f"{key} is a {value}")
hr="hello"
hy=["mohan","sohan","thohan"]
ht={"mohan":"boy","sohan":"man","tohan":"men"}
fun(hr,*hy,**ht)
