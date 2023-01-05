import matplotlib.pyplot as plt
import numpy as np 
import scipy 
import math

from scipy.interpolate import interp1d
print(10**-5)
print (int(math.log10(0.73293)))

x = np.arange(10,20,.1)

print('x:',x)


y = [0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1]

print('y:',y)



f_cubic = scipy.interpolate.interp1d(x,y,kind = 'cubic') 


xnew = np.arange(10,20,.1)


ynew = f_cubic(x)

print('new_x:',xnew)
print('new_y:',ynew)



plt.scatter(x, y, color = 'blue')


plt.plot(xnew, ynew, color = 'black')


plt.xlabel("X")


plt.ylabel("Y")



plt.title("1d Interpolation using scipy interp1d method")


plt.show()




