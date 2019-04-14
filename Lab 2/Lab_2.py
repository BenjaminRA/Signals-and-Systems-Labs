import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Todas las funciones que tienen un "_m" en su nombre, son las funciones aperiodicas, o el objetivo es que esas sean xD
# Y las funciones que están abajo son las que hay que convulsionar.
# Hay que hacer algunos ajustes menores a cada función, pero la idea está :D

def exponential_m(type=False):
    M = 21
    sign = -1 if type else 1
    tau2 = sign*(M-1) / np.log(0.01)
    return signal.exponential(M, 0, tau2, False)

def impulse_m():
    return signal.unit_impulse(20, "mid")

def stair_m():
    u = lambda t: np.piecewise(t, t >= 0, [1,0])
    t = np.arange(-10, 10, 0.1)
    return u(t - 0)

def sine_m():
    senoidal_points = np.arange(100)
    return np.sin(10 * np.pi * senoidal_points / 100) / (10 * np.pi * senoidal_points / 100)

def square():
    square_points = np.linspace(0, 1, 500, endpoint=False)
    return signal.square(10 * np.pi * square_points)

def senoidal():
    senoidal_points = np.linspace(0, 1, 500)
    return np.sin(10 * np.pi * senoidal_points)

def triangle():
    triangle_points = np.linspace(0, 1, 500)
    return signal.sawtooth(10 * np.pi * triangle_points, 0.5)

def convolve(original, filter_impulse):

    filtered = signal.convolve(original, filter_impulse, mode="full", method="direct")

    fig, (ax_orig, ax_win, ax_filt) = plt.subplots(3, 1, sharex=True)
    
    ax_orig.plot(original)
    ax_orig.set_title("Original pulse")
    ax_orig.margins(0, 0.1)

    ax_win.plot(filter_impulse)
    ax_win.set_title("Filter impulse response")
    ax_win.margins(0, 0.1)

    ax_filt.plot(filtered)
    ax_filt.set_title("Filtered signal")
    ax_filt.margins(0, 0.1)
    
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    convolve(
        impulse_m(),
        senoidal()
    )
    # convolve(
    #     np.repeat([0., 1., 0.], 200),
    #     triangle()
    # )
    # example()
    # square()
    # senoidal()
    # triangle()
    # exponential_m()
    # impulse_m()
    # stair_m()
    # sine_m()
