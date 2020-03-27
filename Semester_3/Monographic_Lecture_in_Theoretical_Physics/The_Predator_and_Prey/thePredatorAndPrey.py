# Based on:
# https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations
# https://scipy-cookbook.readthedocs.io/items/LoktaVolterraTutorial.html

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

R0 = 300
F0 = 150
a = 0.01
t = np.linspace(0, 30, 30)

# The SIR model differential equations.
def deriv(y, t, a):
    R, F = y
    dRdt = 2*R - a*R*F
    dFdt = -F + a*R*F

    return dRdt, dFdt

# Initial conditions vector
y0 = R0, F0

ret = odeint(deriv, y0, t, args=(a,))
R, F = ret.T

plt.plot(t, R, color="black", label="Predator")
plt.plot(t, F, color="magenta", label="Prey")

plt.xlabel('Time /days')
plt.ylabel('Agents')
plt.title('The Predator and Prey model')
plt.legend()
plt.savefig("The_Predator_and_Prey.jpg")
