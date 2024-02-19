import matplotlib.pyplot as plt

import numpy as np

from math import factorial

def f(x):
    x = x * 2 * np.pi
    return np.sin(x)


def f_approx(x, order=1, center = 0):
    x = x * 2 * np.pi
    sin_approx = 0
    for i in range(order):
        power = i*2 + 1
        sin_approx += (-1)**(i) * ( (x - center) ** power) / factorial(power)

    return sin_approx



N0 = 1_000

x0 = np.linspace(-1, 2, N0)
y0 = f(x0)
center = 0.5
ya = f_approx(x0, order = 4, center = center)
skip = 10
fig, ax = plt.subplots(figsize=(20,10))

ax.plot(x0, y0, c='b', lw = 1, alpha=0.25)
ax.plot(x0, ya, c='r', lw = 1, alpha=0.25)

N = 50
spacing = 1 / N
offset = spacing * (skip - 1)
print(spacing, offset)
# x = np.linspace(0 - offset, 1 + offset, N + 2*(skip - 1))
x = np.linspace(0, 1, N)

y = f(x)
for i in range(len(x) - skip):
    j = i+skip
    start_point = [x[i], y[i]]
    end_point = [x[j], y[j]]
    points = np.array([start_point, end_point])
    # print(points)
    c = [i/(len(x) - skip)]*3
    ax.plot(points[:,0], points[:,1], c='k')
    # break
# ax.set_xlim(0, 1)
ax.set_ylim(-2, 2)
plt.show()