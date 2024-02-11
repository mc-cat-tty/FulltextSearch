import numpy as np
import matplotlib.pyplot as plt

PRECISION = np.asarray([.3, .3, .3, .3, .5, .5, .5, .0, .0, .0, .0])

r_levels = np.linspace(0.0, 1.0, 11)

ceiling_interp_prec = np.maximum.accumulate(PRECISION[::-1])[::-1]
print(ceiling_interp_prec)

fig, ax = plt.subplots(1, 1)
ax.step(r_levels, ceiling_interp_prec)
ax.step(r_levels, PRECISION)
plt.waitforbuttonpress()
