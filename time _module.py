import time
k=0
intial=time.time()
while k<45:
    print("hello")
   # time.sleep(2) this module is use to wait the output for some second given in bracket after execution of first sataement
    k=k+1
print(time.time()-intial)
intial2=time.time()
for i in range(45):
    print("nmaskar")
print(time.time()-intial2)
