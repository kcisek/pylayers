import matplotlib.pylab as plt 
from pylayers.signal.bsignal import *
i1 = EnImpulse()
i2 = EnImpulse()
i2.translate(-10)
i3 = i1.align(i2)
fig,ax=i3.plot(types=['v'])
plt.show()
