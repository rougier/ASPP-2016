# -----------------------------------------------------------------------------
# Copyright (c) 2016, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# Scientific visualization course
# G-Node 2016 summer school, University of Reading
# Inspired by http://merqur.io/2015/10/02/drawing-a-brain-with-bokeh
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(2007,2014)
Y = [75,75,78,79,80,81,82]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

plt.scatter(X, Y, s=100, color='white', linewidth=2.5, edgecolor='blue', zorder=10)
plt.plot(X,Y, color='blue', linewidth=2.5)

plt.xlim(2006,2014)
plt.xticks(X, ['%d' % x for x in X])

plt.ylim(0,100)
plt.yticks(np.arange(0,101,20), ["%d%%" % x for x in np.arange(0,101,20)])

plt.savefig("exercise-3-sol.png")
plt.show()
