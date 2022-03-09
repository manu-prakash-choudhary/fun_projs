from matplotlib import colors
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np

y=np.array([0.00170,
0.01028,
0.04171,
0.11337,
0.20658,
0.25231,
0.20658,
0.11337,
0.04171,
0.01028,
0.00170])
x=np.array([10,8,6,4,2,0,-2,-4,-6,-8,-10])
x=np.sort(x)
newy=np.array([0.0010,
0.0098,
0.0439,
0.1172,
0.2051,
0.2461,
0.2051,
0.1172,
0.0439,
0.0098,
0.0010])

X_Y_Spline= make_interp_spline(x,y)
plt.axvline(x=0,c="black",)
plt.axhline(y=0,c="black")
plt.xlabel("steps")
plt.ylabel("probabs")

X_=np.linspace(x.min(),x.max(),1000)
Y_ = X_Y_Spline(X_)
X=plt.plot(X_,Y_)
X_Y_Spline= make_interp_spline(x,newy)
Y_ = X_Y_Spline(X_)
labels=["Blue","Red"]
X=plt.plot(X_,Y_,"Red","Blue")
plt.legend(labels)
plt.title("NPD vs BD")
plt.show()
