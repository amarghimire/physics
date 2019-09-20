i=0
j=0
x=[]
y=[]
while i<2:
    z=int(input('type numeric value of x'))
    x.append(z)
    i=i+1
while j<2:
    zz=int(input('type numeric y'))
    y.append(zz)
    j=j+1
print(x)
print(y)

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.ylabel('voltage')
plt.xlabel('frequency')
plt.show()
