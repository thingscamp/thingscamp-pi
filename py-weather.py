# get the pyowm library 
# examples and documentation https://github.com/csparpa/pyowm/wiki/Usage-examples
from pyowm import OWM

# authentication
API_key = "7d1e1ea82891c8bd3e9067781121f41a"
owm = OWM(API_key)

# some shortcuts
obs = owm.weather_at_place('London,uk')             # Toponym
l = obs.get_location()

# getting the weather observations
w = obs.get_weather()
cloud = w.get_clouds()                              # Get cloud coverage
rain = w.get_rain()                                 # Get rain volume
snow = w.get_snow()                                 # Get snow volume
wind = w.get_wind()                                 # Get wind degree and speed
humidity = w.get_humidity()                         # Get humidity percentage
pressure = w.get_pressure()                         # Get atmospheric pressure
temp = w.get_temperature()                          # Get temperature in Kelvin
tempC = w.get_temperature(unit='celsius')           # ... or in Celsius degs
tempF = w.get_temperature('fahrenheit')             # ... or in Fahrenheit degs
status = w.get_status()                             # Get weather short status
detail_status = w.get_detailed_status()             # Get detailed weather status
code = w.get_weather_code()                         # Get OWM weather condition code
icon = w.get_weather_icon_name()                    # Get weather-related icon name
sunrise = w.get_sunrise_time('iso')                 # Sunrise time (GMT UNIXtime or ISO 8601)
sunset = w.get_sunset_time('iso')                   # Sunset time (GMT UNIXtime or ISO 8601)

# metadata
place = l.get_name()
lon = l.get_lon()
lat = l.get_lat()
ID = l.get_ID()

# showing what we got from the api
print "We are getting the weather for ", place
print place, " has longitude ", lon, " and latitude ", lat, "and ID ", ID
print "Observation time: ", obs.get_reception_time(timeformat='iso')   # ISO8601
print "The weather is: \n cloud coverage ... ", cloud
print " rain ... ", rain
print " snow ... ", snow
print " wind degree and speed ... ", wind
print " humidity ... ", humidity
print " atmospheric pressure ... ", pressure
print " temperature in Celsius ... ", tempC
print " temperature in Farenheit ...", tempF
print " short weather status ... ", status
print " detailed weather status ...", detail_status
print " OWM weather condition code ...", code
print " OWM weather icon name ...", icon
print " sunrise time ...", sunrise
print " sunset time ...", sunset