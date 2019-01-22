#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


width = 0.2
height = 0.15
x = 0.5
y = 0.5
z = 0.5
radius = 0.2

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

support_patch = mpatches.Rectangle(
    (x - width * 0.5, z - width * 0.5), width, height,  hatch='//', linewidth=0, color=('#f6d04d7f'),  zorder=9)

support_patch2 = mpatches.RegularPolygon((x, y - radius),
                                         numVertices=3, radius=radius, color='r', zorder=9)

ax1.add_patch(support_patch)
ax1.add_patch(support_patch2)
plt.show()


# import matplotlib.pyplot as plt

# """ A first plot - get some numbers, plot them against
# a uniform X axis starting at 1 using all the defaults."""


# plt.plot([1, 23, 2, 4])
# plt.ylabel('some numbers')

# plt.show()
