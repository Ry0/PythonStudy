import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def test_plot():
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)
    plt.plot(t, s)

    plt.title('About as simple as it gets, folks')

    plt.show()


if __name__ == "__main__":
    print(matplotlib.get_backend())
    print(matplotlib.matplotlib_fname())
    test_plot()
