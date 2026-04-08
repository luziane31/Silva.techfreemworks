import numpy as np
import matplotlib.pyplot as plt

# Constantes
a0 = 1.732e-3
f0 = 27.6322e6
c = 3e8

def potential_V(a, lambda0=1.0, B=1.0, C=1.0, Lambda0=0.01):
    return (lambda0 / a**4) + (B / a**6) - (C / a**2) + (Lambda0 * a**3)

def calculate_frequency(a):
    return c / (2 * np.pi * a)

if __name__ == "__main__":
    a_values = np.logspace(-6, -2, 500)
    V_values = potential_V(a_values)

    f_calc = calculate_frequency(a0)

    print("Calculated Frequency:", f_calc)

    plt.plot(a_values, V_values)
    plt.xscale("log")
    plt.title("Silva-Tech Potential")
    plt.show()
