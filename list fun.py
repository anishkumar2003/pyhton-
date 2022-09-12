num=[55,45,67,65,78,90]

# enumerate function is uesd to print value as well as index value
for v in enumerate(num):
    print(v)
if all([i>5 for i in num]):
    print("all larger than five")
if any([i%2==0 for i in num]):
    print("even")
