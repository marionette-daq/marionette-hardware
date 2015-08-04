#  Compute the transfer function and loop stability for the TPS40200
#  in the Zeta configuration.
#  

from __future__ import division
from scipy import *
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import pdb
from numpy import pi

pdb.set_trace()

DATAPOINTS = 100 
gbw = np.log10(1.5E6)  # Gain Band Width log of Error Amplifier
f = np.zeros(DATAPOINTS)
f=np.logspace(0,7,DATAPOINTS)  #log array, 10**0 to 10**8, 100 points
S=2.0*pi*f*1j

L1a = 8.E-6
Cc = 22.E-6
L1b = 8.E-6
Cout = 22.E-6
R1 = 90.9E3   #top feedback resistor
R2 = 15.E3   # bottom feedback resistor - TPS40200 has VREF = 700mV
R3 = 10.E3   # compensation resistor in parallel with R1
Cp = 1.6E-8  # compensation cap in parallel with R1, series with R3
Rload = 10    # load resistance is about 10 ohms

Kpwm = 10   # Modulator gain is flat 10 across bandwidth (pg 24)

# Error Amplifier calculations
Kea = np.zeros(DATAPOINTS, dtype=complex)
for idx in range(0, len(f)):
    log_freq = np.log10(f[idx])
    error_amp_gain = 10**(gbw-log_freq)
    if (f[idx] < 1500):
        Kea[idx] = 1000
    else:
        Kea[idx] = error_amp_gain

#LP output filter
lp = np.zeros(DATAPOINTS, dtype=complex)
for idx in range(0, len(f)):
    lp[idx] = 1./((S[idx]**2)*L1b*Cout+1)

#HP filter
hp = np.zeros(DATAPOINTS, dtype=complex)
for idx in range(0, len(f)):
    hp[idx] = ((S[idx]**2)*L1a*Cc+1)/((S[idx]**2)*L1a*Cc)

# Calculate the open loop transfer function G(s) 
G = np.zeros(DATAPOINTS, dtype=complex)
for idx in range(0, len(f)):
    G[idx] = Kea[idx]*Kpwm*hp[idx]*lp[idx]

# Calculate the feedback transfer function B(s)
B = np.zeros(DATAPOINTS, dtype=complex)
for idx in range(0, len(f)):
    B[idx] = (S[idx]*R1*Cp*(R2+R3)+R1)/\
        ((S[idx]*R1*Cp*(R2+R3)+R1)+S[idx]*R2*R3*Cp+R2)

# Calculate the closed loop transfer function 
Tv = np.zeros(DATAPOINTS, dtype=complex)
for idx in range(0, len(f)):
    Tv[idx] = G[idx]/(1+G[idx]*B[idx])

# Sanity check
easy_transfer = np.zeros(DATAPOINTS, dtype=complex)
for idx in range(0, len(f)):
    easy_transfer[idx] = (1+.0001*S[idx])/(S[idx])

func_to_plot = hp
figure(1)
clf()# clear the figure
subplot(211)
title('Zeta tps40200 transfer function')
semilogx(f,20*np.log10(abs(func_to_plot)))
ylabel('Mag. Ratio (dB)')

subplot(212)
semilogx(f,arctan2(imag(func_to_plot),real(func_to_plot))*180.0/pi)
ylabel('Phase (deg.)')
xlabel('Freq (Hz)')

show()
