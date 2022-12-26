import matplotlib.pyplot as plt
import numpy as np 
import scipy 

from scipy.interpolate import interp1d


x = np.arange(10,20)

print('x:',x)


y = np.exp(-x/10)

print('y:',y)



f_cubic = scipy.interpolate.interp1d(x,y,kind = 'cubic') 


xnew = np.arange(10,19,0.1)


ynew = f_cubic(xnew) 

print('new_x:',xnew)
print('new_y:',ynew)



plt.scatter(x, y, color = 'blue')


plt.plot(xnew, ynew, color = 'black')


plt.xlabel("X")


plt.ylabel("Y")



plt.title("1d Interpolation using scipy interp1d method")


plt.show()


