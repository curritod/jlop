import numpy as np
import matplotlib.pyplot as plt

from jlop.ratios import golden_ratio, silver_ratio
from jlop import set_colorcycle

#The following 3 styles are avaliable:
plt.style.use('jlop')
#plt.style.use('jlop_modern')
#plt.style.use('jlop70')

#The following color schemes are avaliable#
colors = set_colorcycle(name='pc-88')
#colors = set_colorcycle(name='catppuccin')
#colors = set_colorcycle(name='secam')
#colors = set_colorcycle(name='cga')
#colors = set_colorcycle(name='coldwood')
#colors = set_colorcycle(name='clement-8')
#colors = set_colorcycle(name='sweethope')
#colors = set_colorcycle(name='vivid-memory')
#colors = set_colorcycle(name='fairydust')
#colors = set_colorcycle(name='vibrant14')

#Create a simple figure

fig, ax = plt.subplots(figsize=((3+3/8),(3+3/8)/golden_ratio), dpi=300, layout='constrained')

ax.set_xlabel('$x$-label')
ax.set_ylabel('$y$-label')

x = np.linspace(0,4*np.pi,100)
for n in range(1,10):
    ax.plot(x,np.cos(x)+n, label=None)

fig.savefig('./figures/preview.png')
