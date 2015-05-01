import serial
import time

time_between_samples = 1 #s

time_to_run = 301 #s

# change the first argument to be a number correpsonding to
# the COM port on windows or to be the string '/dev/ttyACMX' where ttyACMX is
# the name of the device on unix.
arduino_port = serial.Serial(2, baudrate=9600, timeout=1)

# wait for the duino to wake from reset
time.sleep(1)

output_file = open("temperature_log.txt", "a")

start_time = time.time() #s
current_time = 0

while (time.time() - start_time) < time_to_run:
    
    # wait until 1 second has elapsed since the last sample
    while (time.time() - start_time) < (current_time + time_between_samples):
        pass

    # ask for a data point
    arduino_port.write('a')
    new_data_point = arduino_port.read(11)
    current_time += time_between_samples
    exact_sample_time = time.time() - start_time
    print current_time, exact_sample_time, new_data_point

    # append to the log file, which is in append mode for writes
    output_file.write(str(exact_sample_time) + "," + new_data_point)

arduino_port.close()
output_file.close()
