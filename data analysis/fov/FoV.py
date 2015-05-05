import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit


def model(d, FoV, k):
    bowl_diam = 5
    max_d = bowl_diam*0.5 / math.tan(FoV*0.5*math.pi/180)
    if d < max_d:
        return 0
    diff = np.subtract(d, max_d)
    return diff*k

distances = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
distances = [d*2.54 for d in distances]
temperatures = [-1.9, -1, 0, 0.7, 1.2, 2.9, 3.5, 5.2, 9.2, 12.3, 13.8]

popt, pcov = curve_fit(model, distances, temperatures)
distances2 = np.linspace(0, 5)
distances2 = [d*2.54 for d in distances2]
temperatures2 = [model(x, *popt) for x in distances2]

print "Field of view is estimated to be " + str(popt[0])[:5] + " degrees."

plt.plot(distances, temperatures, 'o')
plt.plot(distances2, temperatures2, linestyle='--')

plt.xlabel('Distance (mm)')
plt.ylabel('Temperature Reading ($\degree$C)')
plt.title('Temperature Readings from a Distance')

plt.show()


