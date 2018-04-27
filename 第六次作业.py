import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus']=False

plt.figure(figsize=(9,9))

X = np.array([0,1,2,3,-1,-2,-3])
Y = np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])
x = np.linspace(X.min()* 1.1, X.max() * 1.1,2000)


def func(p, x):
    a, b, c = p
    return a * x ** 2 + b * x + c


def err(p, x, y):
    return func(p, x) - y

p0=[1,1,1]
exceptp=leastsq(err,p0,args=(X,Y))
a,b,c=exceptp[0]

y = a * x * x + b * x + c

plt.scatter(X,Y, s=100, alpha=1.0, marker='o',label='数据点')
plt.plot(x, y, color='r',linewidth=5, linestyle=":",markersize=20, label='拟合曲线')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel('安培/A')
plt.ylabel('伏特/V')

plt.xlim(x.min(), x.max())
plt.ylim(0, y.max() * 1.1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')

plt.show()
