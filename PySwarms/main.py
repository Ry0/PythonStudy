from pyswarms.single.global_best import GlobalBestPSO
import numpy as np
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx


def rosenbrock_with_args(x, a, b, c):
    f = (a - x[:, 0]) ** 2 + c * (b - x[:, 1]) ** 2
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
    rosenbrock_with_args, 1000, a=1, b=56, c=4)
