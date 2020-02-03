import numpy as np
import matplotlib.pyplot as plt

# Our data...
x = np.linspace(0, 10, 100)
y1, y2, y3 = np.cos(x), np.cos(x + 1), np.cos(x + 2)
names = ['Signal 1', 'Signal 2', 'Signal 3']

data = [y1, y2, y3]
fig, axes = plt.subplots(nrows = 3,ncols = 1)

for i in range(len(axes)):
    axes[i].set_title(names[i])
    axes[i].plot(data[i], 'k')
    axes[i].set_xticks([])
    axes[i].set_yticks([])
    axes[i].margins(0)

plt.show()
