
"""
File Reading and Writing
Let's take our previous example (taking measurements from an I2C device) and log them to a file!
This can be incredibly useful if you are trying to measure the temperature (light, humidity, wind speed, air pressure, people entering your room,
or really anything) and want to see how it changes over the course of minutes, hours, or days.

"""

"""
HARDWARE Connections :
Connect SDA1 (GPIO2, pin 3) to SDA on the TMP102
Connect SCL1 (GPIO3, pin 5) to SCL on the TMP102
Connect power (3.3 V) to VCC on the TMP102
Connect ground (GND) to GND on the TMP102
"""


import time
import datetime
import tmp102




filename = "temp_log.csv"

# Create header row in new CSV file
csv = open(filename, 'w')
csv.write("Timestamp,Temperature\n")
csv.close

# Initialize communication with TMP102
tmp102.init()






# Sample temperature every second for 10 seconds
for t in range(0, 10):

    # Construct CSV entry from timestamp and temperature
    temp_c = str(round(tmp102.read_temp(), 2))
    entry = str(datetime.datetime.now())
    entry = entry + "," + temp_c + "\n"

    # Log (append) entry into file
    csv = open(filename, 'a')
    try:
        csv.write(entry)
    finally:
        csv.close()

    # Wait 1 second before sampling temperature again
    time.sleep(1)

# When all the writing has been completed, print the CSV contents
csv = open(filename, 'r')
print(csv.read())
csv.close()





"""
nothing happen for 10 seconds as the program reads the temperature once every second.
For fun, try breathing on the temperature sensor to affect the data! After those 10 seconds,
the collection should be complete, and the contents of temp_log.csv will be printed to the screen.

"""
