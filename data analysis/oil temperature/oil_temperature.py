import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit

import csv
import time

points_save15 = []
timestamps_save15 = []
tc_temperatures_save15 = []

with open('save15.csv') as csvfile:
    foo_reader = csv.reader(csvfile, delimiter=',')
    for row in foo_reader:
        points_save15.append(int(row[0]))
        timestamps_save15.append(row[1])
        tc_temperatures_save15.append(float(row[2]))

points_save16 = []
timestamps_save16 = []
tc_temperatures_save16 = []

with open('save16.csv') as csvfile:
    foo_reader = csv.reader(csvfile, delimiter=',')
    for row in foo_reader:
        points_save16.append(int(row[0]))
        timestamps_save16.append(row[1])
        tc_temperatures_save16.append(float(row[2]))

points_save17 = []
timestamps_save17 = []
tc_temperatures_save17 = []

with open('save17.csv') as csvfile:
    foo_reader = csv.reader(csvfile, delimiter=',')
    for row in foo_reader:
        points_save17.append(int(row[0]))
        timestamps_save17.append(row[1])
        tc_temperatures_save17.append(float(row[2]))

times_log_oil1 = []
ambient_temps_log_oil1 = []
ir_temps_log_oil1 = []

with open('temperature_log_oil1.txt') as f:
    contents = list(f.read())

    while len(contents) != 0:

        # first, get the time
        c = contents.pop(0)
        s = ''
        while c != ',':
            s += c
            c = contents.pop(0)
        times_log_oil1.append(float(s))

        # then, ambient temp
        c = contents.pop(0)
        s = ''
        while c != ',':
            s += c
            c = contents.pop(0)
        ambient_temps_log_oil1.append(float(s))

        # then, ir temp
        c = contents.pop(0)
        s = ''
        while c != '.':
            s += c
            c = contents.pop(0)
        s += c
        c = contents.pop(0)
        s += c
        c = contents.pop(0)
        s += c
        ir_temps_log_oil1.append(float(s))
        
times_log_oil2 = []
ambient_temps_log_oil2 = []
ir_temps_log_oil2 = []

with open('temperature_log_oil2.txt') as f:
    contents = list(f.read())

    while len(contents) != 0:

        # first, get the time
        c = contents.pop(0)
        s = ''
        while c != ',':
            s += c
            c = contents.pop(0)
        times_log_oil2.append(float(s))

        # then, ambient temp
        c = contents.pop(0)
        s = ''
        while c != ',':
            s += c
            c = contents.pop(0)
        ambient_temps_log_oil2.append(float(s))

        # then, ir temp
        c = contents.pop(0)
        s = ''
        while c != '.':
            s += c
            c = contents.pop(0)
        s += c
        c = contents.pop(0)
        s += c
        c = contents.pop(0)
        s += c
        ir_temps_log_oil2.append(float(s))
        
  
times_log_oil3 = []
ambient_temps_log_oil3 = []
ir_temps_log_oil3 = []

with open('temperature_log_oil3.txt') as f:
    contents = list(f.read())

    while len(contents) != 0:

        # first, get the time
        c = contents.pop(0)
        s = ''
        while c != ',':
            s += c
            c = contents.pop(0)
        times_log_oil3.append(float(s))

        # then, ambient temp
        c = contents.pop(0)
        s = ''
        while c != ',':
            s += c
            c = contents.pop(0)
        ambient_temps_log_oil3.append(float(s))

        # then, ir temp
        c = contents.pop(0)
        s = ''
        while c != '.':
            s += c
            c = contents.pop(0)
        s += c
        c = contents.pop(0)
        s += c
        c = contents.pop(0)
        s += c
        ir_temps_log_oil3.append(float(s))
        

#plt.plot(tc_temperatures_save15 + tc_temperatures_save16 + tc_temperatures_save17)
#plt.plot(ir_temps_log_oil1 + ir_temps_log_oil2 + ir_temps_log_oil3)

x = tc_temperatures_save15 + tc_temperatures_save16 + tc_temperatures_save17
y = ir_temps_log_oil1 + ir_temps_log_oil2 + ir_temps_log_oil3

# i had to throw out some malformed data from the ir sensor, so here's truncated x
x = x[:len(y)]

plt.plot(x, y, '.')

plt.xlabel('Oil Bath Temperature ($\degree$C)')
#plt.ylabel('$\degree$C')
plt.title('Temperature Readings of an Oil Bath')

differences = [abs(z[0] - z[1]) for z in zip(x, y)]
mean_difference = sum(differences)/len(differences)
print mean_difference

plt.plot(x, differences, '.')

plt.legend(['IR Temperature Reading ($\degree$C)', 'Absolute Error ($\degree$C)'], loc='top left')

plt.show()
