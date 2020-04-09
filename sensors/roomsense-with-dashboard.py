# basic room sensors circuit
# temperature, light level and movement

# import libraries
import time
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT as dht
import urllib2
import urllib
import httplib
import datetime

# set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# variables for the readings
PinTemp = 4
PinLight = 27
PinMove = 17

# a function for reading the light level
def ReadLight():
    LDRCount = 0
    GPIO.setup(PinLight, GPIO.OUT)
    GPIO.output(PinLight, GPIO.LOW)
    time.sleep(0.1) # drains all charge from the capacitor
    GPIO.setup(PinLight, GPIO.IN) # sets the pin to be input
    # while the input pin reads 'off' or Low, count
    while (GPIO.input(PinLight) == GPIO.LOW):
        LDRCount += 1 # add one to the counter
    return LDRCount

# a function for reading the temperature and humidity via DHT11 sensor
#def getSensorData():
#    RH, T = dht.read_retry(dht.DHT11, 18)
#    #return RH, T # returns tuple in ('parentheses and quotes')
#    return ("{0:0.1f}, {1:0.1f}".format(RH, T)) # returns tuple in 'quotes'
#    #return int(RH), int(T) returns tuple in (parentheses)

# function to read only temperature
def ReadTemp():
    RH, T = dht.read_retry(dht.DHT11, 18)
    return T

# function to read only humidity
def ReadHum():
    RH, T = dht.read_retry(dht.DHT11, 18)
    return RH

# a function for reading the PIR state
def ReadMove():
    # set PIR pin as input
    GPIO.setup(PinMove, GPIO.IN)
    return GPIO.input(PinMove)

while True:
    # variable string to hold all the readings
    now = datetime.datetime.now()
    readings = (ReadLight(), ReadMove(), ReadTemp(), ReadHum(), now.isoformat())
    fname = "roomsense.csv"
    target = open(fname, 'a')    
    target.write(str(readings))
    target.write("\n")
    print ("Read ok"), (now.isoformat(), ReadLight(), ReadMove(), ReadTemp(), ReadHum())
    target.close()
    time.sleep(5) # wait for sixteen seconds
    ##params = urllib.urlencode({'field1': ReadLight(), 'field2': ReadTemp(), 'field3': ReadHum(), 'field4': ReadMove(), 'key':'your_key_here'})
    #headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    #conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        #conn.request("POST", "/update", params, headers)
        #response = conn.getresponse()
        print ReadLight()
        print ReadTemp()
        print ReadHum()
        print ReadMove()
        ##print response.status, response.reason
        #data = response.read()
        #conn.close()
    except:
        print "Connection failed :("

#    GPIO.cleanup()
