import random
x =random.randint(1, 100)  
ciag = []
ciag.append(x)
while x >1:
    if x %2 ==0:
        x=int(x/2)
        ciag.append(x)
    else:
         x=3*x+1
         ciag.append(x)
print(ciag)        