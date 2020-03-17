from pyswarms.single.global_best import GlobalBestPSO
import numpy as np
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
from pyswarms.utils.plotters.formatters import Mesher, Designer
import matplotlib.pyplot as plt


def rosenbrock_with_args(x, a, b, c):
    int_x = np.array(x, dtype=int)
    f = (a - int_x[:, 0]) ** 2 + c * (b - int_x[:, 1]) ** 2
    return f


# instatiate the optimizer
x_max = 100 * np.ones(2)
x_min = -1 * x_max
bounds = (x_min, x_max)
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
optimizer = GlobalBestPSO(
    n_particles=10,
    dimensions=2,
    options=options,
    bounds=bounds)

# now run the optimization, pass a=1 and b=100 as a tuple assigned to args

cost, pos = optimizer.optimize(
    rosenbrock_with_args, 50, a=6, b=17, c=4)
# plot_cost_history(optimizer.cost_history)


# m = Mesher(func=fx.sphere,
#            limits=[(-1, 1), (-1, 1)])
# # Adjust figure limits
# d = Designer(limits=[(-1, 1), (-1, 1), (-0.1, 1)],
#              label=['x-axis', 'y-axis', 'z-axis'])
# plot_contour(pos_history=optimizer.pos_history,
#              mesher=m, designer=d, mark=(0, 0))
# plt.show()
