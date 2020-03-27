# Based on
# Theory:
# https://ibmathsresources.com/2014/05/17/modelling-infectious-diseases/
# https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model
# http://mat.uab.cat/matmat/PDFv2013/v2013n03.pdf
# Theory + code:
# https://scipython.com/book/chapter-8-scipy/additional-examples/the-sir-epidemic-model/


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Number of agents, 37 169 - the population of Oleśnica (city in Poland).
N = 37169
# Initial number of infected.
I0 = 1
# Initial number of recovered.
R0 = 0
# The rest of the people exposed to the virus initially.
S0 = N - I0 - R0
# Contact rate.
beta = 0.3
# Mean recovery rate 1/days
gamma = 1./10
# A grid of time points (in days)
t = np.linspace(0, 365, 365)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T



plt.plot(t, S, label="Susceptible")
plt.plot(t, I, color="red", label="Infected")
plt.plot(t, R,  label="Recovered/Immune")
plt.xlabel('Time /days')
plt.ylabel('Agents')
plt.title('The SIR model, beta = 0.3')
plt.legend()
plt.savefig("SIR_b_030.jpg")
