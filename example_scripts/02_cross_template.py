import numpy as np
import matplotlib as plt
from jlop import set_colorcycle
from jlop.templates import cross_plot

plt.style.use('jlop')
set_colorcycle('catppuccin')

fig, ax = cross_plot(xlabel='$\\alpha$', ylabel='$\\beta$', xlim=[0,16],ylim=[-8,8], ticks_frequency=2)


t = np.linspace(0,1*2*np.pi,100)

for n in range(1,10):
    x = 8+5*np.cos(n+t)
    y = 8*np.sin(t)
    ax.plot(x,y, label=None)

fig.savefig('./figures/cross_plot.png')

