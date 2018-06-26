import numpy as np
import matplotlib.pyplot as plt
import scipy as sc


x=np.linspace(-5,5,20)
y=x**2
print y,x
plt.plot(x,y,'.-r')

plt.savefig('plot.png')
plt.show()
plt.clf()
plt.scatter(x,np.exp(x))
plt.show()

#a=5
#print 'La raiz cuadrada de 5 es:', np.sqrt(a)
