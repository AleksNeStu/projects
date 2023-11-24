import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl


fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

plt.show()

#Note that to get this Figure to display, you may have to call plt.show(), depending on your backend. For more details of Figures and backends, see Introduction to Figures.

fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# a figure with one axes on the left, and two on the right:
fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])
plt.show()