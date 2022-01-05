from math import *
s=0
for d in range(10):
    for u in range(10):
        while (d+u+3>=15) and u%2==0:
            s=s+1;
            n=d*pow(10,2)+10*u+3;
            print(n);
            break
print(s)

         
