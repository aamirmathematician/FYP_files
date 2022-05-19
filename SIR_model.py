# -*- coding: utf-8 -*-
"""
Created on Mon May 16 23:50:03 2022

@author: Aamir Ali
"""

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


# Interval of Computation
a = 0;
b = 400;
h = 0.1; # Step size in the interval.

# Constants
N = 3.28196e8
beta = 0.1205  # infected person infects 1 other person per day
#D = 6.0 # infections lasts four days
gamma =  0.066 #1.0 / D

S0, I0, R0 = N-1000, 1000, 0  # initial conditions: one infected, rest susceptible


l = int((b-a)/h);
t = np.linspace(0, 400, l) # Grid of time points (in days)
y0 = S0,I0, R0  # Initial conditions vector

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T


#plotting fig1
plt.figure(figsize=(15, 10))  
plt.plot(t, S, 'b', linewidth=4, label = 'Susceptible')
plt.plot(t, I, 'r', linewidth=4, label='Infected')
plt.plot(t, R, 'k', linewidth=4, label='Recovered')
plt.rcParams.update({'font.size': 45})
#plt.title("Susceptible and Recovered")

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.xlabel("Time(Days)")
plt.ylabel("Number of People")
plt.legend(['Susceptible','Infected','Recovered'])
