import numpy as np
import pyswarms as ps
from pyswarms.utils.plotters import plot_cost_history, plot_contour, plot_surface
from pyswarms.utils.plotters.formatters import Mesher, Designer
import matplotlib.pyplot as plt


def return_digit(num):
    i = 1
    base_num = 1
    while True:
        base_num = 2 * base_num
        if base_num > num:
            break
        i += 1
    return i


def return_decimal(ary):
    result = 0
    for i in range(ary.shape[0]):
        result += ary[i] * 2**i
    return result


def rosenbrock_with_args(x, a, b, c):
    f = (a - x[:, 0]) ** 2 + c * (b - x[:, 1]) ** 2
    return f


def f_per_particle(x, a, b, c):
    x1 = x[0:5]
    x2 = x[5:10]
    x1_10 = return_decimal(x1)
    x2_10 = return_decimal(x2)
    f = (a - x1_10) ** 2 + c * (b - x2_10) ** 2
    return f


def f(x, a, b, c):
    """Higher-level method to do classification in the
    whole swarm.

    Inputs
    ------
    x: numpy.ndarray of shape (n_particles, dimensions)
        The swarm that will perform the search

    Returns
    -------
    numpy.ndarray of shape (n_particles, )
        The computed loss for each particle
    """
    n_particles = x.shape[0]
    j = [f_per_particle(x[i], a, b, c) for i in range(n_particles)]
    return np.array(j)


def main():
    # instatiate the optimizer
    options = {'c1': 0.5, 'c2': 0.5, 'w': 0.9, 'k': 50, 'p': 2}
    optimizer = ps.discrete.BinaryPSO(
        n_particles=50,
        dimensions=10,
        options=options)

    # now run the optimization, pass a=1 and b=100 as a tuple assigned to args

    cost, pos = optimizer.optimize(
        f, 25, a=6, b=17, c=4)
    # plot_cost_history(optimizer.cost_history)
    x1 = pos[0:5]
    x2 = pos[5:10]
    x1_10 = return_decimal(x1)
    x2_10 = return_decimal(x2)
    print(x1_10)
    print(x2_10)

    # m = Mesher(func=fx.sphere,
    #            limits=[(-1, 1), (-1, 1)])
    # # Adjust figure limits
    # d = Designer(limits=[(-1, 1), (-1, 1), (-0.1, 1)],
    #              label=['x-axis', 'y-axis', 'z-axis'])
    # plot_contour(pos_history=optimizer.pos_history,
    #              mesher=m, designer=d, mark=(0, 0))
    # plt.show()


if __name__ == "__main__":
    main()
