# Program checks basic libraries needed to proceed with data analysis using python
import matplotlib
import numpy as np
import scipy.linalg
import pylab as plt

print np.__version__
print scipy.__version__
print matplotlib.__version__

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
a = scipy.linalg.eig(([[1, 2], [3, 4]]))
plt.show()

