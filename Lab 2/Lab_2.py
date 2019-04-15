import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Todas las funciones que tienen un "_m" en su nombre, son las funciones aperiodicas, o el objetivo es que esas sean xD
# Y las funciones que están abajo son las que hay que convulsionar.
# Hay que hacer algunos ajustes menores a cada función, pero la idea está :D
# Pongo el valor en el pivote que es el 0 (donde reflejé la función)

def exponential_m(decay=False):
    """
    Returns an exponential function.

    Parameters
    ----------
    decay: bool
        If True returns a decaying exponential function
        If False returns a growing exponential function
    """
    
    M = 50
    sign = -1 if type else 1
    tau2 = sign*(M) / np.log(0.1)
    return signal.exponential(M, 0, tau2, False)

def impulse_m():
    """
    Returns a single impulse signal.
    """
    
    return signal.unit_impulse(3, "mid")

def stair_m():
    """
    Returns the stair function with origin at zero.
    """
    
    u = lambda t: np.piecewise(t, t >= 0, [1,0])
    t = np.arange(-10, 10, 1)
    return u(t)

def sine_m():
    """
    Returns an aperiodic sinusoidal function.
    """
    
    senoidal_points = np.linspace(0, 1, 500)
    return np.sin(10 * np.pi * senoidal_points) / 10 * np.pi * senoidal_points

def square():
    """
    Returns a square function.
    """
    
    square_points = np.linspace(0, 1, 500, endpoint=False)
    return signal.square(10 * np.pi * square_points)

def sine():
    """
    Returns a periodic sinusoidal function.
    """
    
    senoidal_points = np.linspace(0, 1, 500)
    return np.sin(10 * np.pi * senoidal_points)

def triangle():
    """
    Returns a triangle or sawtooth function.
    """
    
    triangle_points = np.linspace(0, 1, 500)
    return signal.sawtooth(10 * np.pi * triangle_points, 0.5)

def convolve(original, filter_impulse, multiplier = 1, offset = 0):
    """
    Convolves two signals and plots the original signal, 
    the filter impulse response signal and the filtered signal in the same figure.

    Parameters
    ----------
    original : array.
            Original Input.
    filter_impuse : array
            Filter Impulse Response.
    multiplier: num
            Multiplies the filter impulse response by this factor.
    offset: int
            contatenates this amount of 0 before de filter impulse response
    """

    filter_impulse = [*np.linspace(0, 0, offset), *filter_impulse]

    filter_impulse = np.asarray(filter_impulse) * multiplier

    filtered = signal.convolve(original, filter_impulse, mode="full")

    fig, (ax_orig, ax_win, ax_filt) = plt.subplots(3, 1)
    
    ax_orig.plot(original)
    ax_orig.grid(True)
    ax_orig.set_title("Entrada")
    ax_orig.set_xlabel('Tiempo (t)')
    ax_orig.set_ylabel('Valor')
    ax_orig.margins(0, 0.1)

    ax_win.plot(filter_impulse)
    ax_win.set_title("Función de Transferencia")
    ax_win.grid(True)
    ax_win.set_xlabel('Tiempo (t)')
    ax_win.set_ylabel('Valor')
    ax_win.margins(0, 0.1)

    ax_filt.plot(filtered)
    ax_filt.grid(True)
    ax_filt.set_title("Salida")
    ax_filt.set_xlabel('Tiempo (t)')
    ax_filt.set_ylabel('Valor')
    ax_filt.margins(0, 0.1)
    
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    convolve(triangle(), stair_m())
