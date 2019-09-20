i=0
j=0
x=[]
y=[]
while i<3:
    z=int(input('type numeric x'))
    x.append(z)
    i=i+1
while j<3:
    zz=int(input('type numeric y'))
    y.append(zz)
    j=j+1
print(x)
print(y)
import matplotlib.pyplot as plt
plot(x,y,'ro')
# plt.axis([0, 6, 0, 20])
plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()