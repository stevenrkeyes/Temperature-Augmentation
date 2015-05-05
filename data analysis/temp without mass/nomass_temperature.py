import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit

import csv
from operator import itemgetter

points_save37 = []
timestamps_save37 = []
tc_temperatures_save37 = []

with open('save37.csv') as csvfile:
    foo_reader = csv.reader(csvfile, delimiter=',')
    for row in foo_reader:
        points_save37.append(int(row[0]))
        timestamps_save37.append(row[1])
        tc_temperatures_save37.append(float(row[2]))

points_save39 = []
timestamps_save39 = []
tc_temperatures_save39 = []

with open('save39.csv') as csvfile:
    foo_reader = csv.reader(csvfile, delimiter=',')
    for row in foo_reader:
        points_save39.append(int(row[0]))
        timestamps_save39.append(row[1])
        tc_temperatures_save39.append(float(row[2]))

points_save40 = []
timestamps_save40 = []
tc_temperatures_save40 = []

with open('save40.csv') as csvfile:
    foo_reader = csv.reader(csvfile, delimiter=',')
    for row in foo_reader:
        points_save40.append(int(row[0]))
        timestamps_save40.append(row[1])
        tc_temperatures_save40.append(float(row[2]))

points_save41 = []
timestamps_save41 = []
tc_temperatures_save41 = []

with open('save41.csv') as csvfile:
    foo_reader = csv.reader(csvfile, delimiter=',')
    for row in foo_reader:
        points_save41.append(int(row[0]))
        timestamps_save41.append(row[1])
        tc_temperatures_save41.append(float(row[2]))

# trim the data
tc_temperatures_save41 = tc_temperatures_save41[4:]
tc_temperatures_save37 = tc_temperatures_save37[:20]

tc_temperatures_save37 = [(t-32)/1.8 for t in tc_temperatures_save37]
tc_temperatures_save39 = [(t-32)/1.8 for t in tc_temperatures_save39]
tc_temperatures_save40 = [(t-32)/1.8 for t in tc_temperatures_save40]
tc_temperatures_save41 = [(t-32)/1.8 for t in tc_temperatures_save41]

plt.plot(tc_temperatures_save40)
plt.plot(tc_temperatures_save39)
plt.plot(tc_temperatures_save41)
plt.plot(tc_temperatures_save37)

plt.xlabel("Time (s)")
plt.ylabel("Temperature ($\degree$C)")
plt.title("Cold Side Temperature of a Peltier Device\nin Room Temperature Air")

plt.legend(["1 device, 0.8A, 9V",
            "2 devices, stacked, 0.8A, 9V each",
            "3 devices, stacked, 0.6A, 9V each",
            "1 device 4A, 12V"])

minimum_1_8_9 = min(enumerate(tc_temperatures_save40), key=itemgetter(1))
minimum_2_8_9 = min(enumerate(tc_temperatures_save39), key=itemgetter(1))
minimum_3_6_9 = min(enumerate(tc_temperatures_save41), key=itemgetter(1))
minimum_1_4_12 = min(enumerate(tc_temperatures_save37), key=itemgetter(1))

def rise_time(data):
    mins = min(enumerate(data), key=itemgetter(1))
    # values at 20% and 80%
    v_0 = data[0]
    v_10 = (v_0 - mins[1])*.1 + mins[1]
    v_90 = (v_0 - mins[1])*.9 + mins[1]
    
    t_10 = min(enumerate(data[:mins[0]]), key=lambda x:abs(itemgetter(1)(x)-v_10))
    t_90 = min(enumerate(data[:mins[0]]), key=lambda x:abs(itemgetter(1)(x)-v_90))
    t_rise = (t_10[0] - t_90[0])/2.2

    return t_rise
    

print "minimum for 1 device, 0.8A, 9V:", minimum_1_8_9[1], "at time", minimum_1_8_9[0], "sec; time constant", rise_time(tc_temperatures_save40)
print "minimum for 2 devices, 0.8A, 9V:", minimum_2_8_9[1], "at time", minimum_2_8_9[0], "sec; time constant", rise_time(tc_temperatures_save39)
print "minimum for 3 devices, 0.6A, 9V:", minimum_3_6_9[1], "at time", minimum_3_6_9[0], "sec; time constant", rise_time(tc_temperatures_save41)
print "minimum for 1 device, 4A, 12V:", minimum_1_4_12[1], "at time", minimum_1_4_12[0], "sec; time constant", rise_time(tc_temperatures_save37)

plt.show()


