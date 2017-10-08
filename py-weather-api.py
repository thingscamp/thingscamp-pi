from pyowm import OWM

API_key = "7d1e1ea82891c8bd3e9067781121f41a"
owm = OWM(API_key)

    
# Find observed weather in all the "London"s in the world
#obs_list = owm.weather_at_places('London', 'accurate')
#print "obs_list \n", obs_list, "\n"
# As above but limit result items to 3
#obs_list3 = owm.weather_at_places('London',searchtype='accurate',limit=3)
#print "obs_list_3 \n", obs_list3, "\n"

# Find observed weather for all the places whose name contains the word "London"
#obs_list_LDN = owm.weather_at_places('London', 'like')
#print "obs_list_LDN \n", obs_list_LDN, "\n"
# As above but limit result items to 5
#obs_list_like = owm.weather_at_places('London', 'like', 5)
#print "obs_list_like \n", obs_list_like, "\n"

# Find observed weather for all the places in the surroundings of lon=-2.15,lat=57
#obs_list_coord = owm.weather_around_coords(-2.15, 57)
#print "obs_list_coord \n", obs_list_coord, "\n"
# As above but limit result items to 8
#obs_list_near = owm.weather_around_coords(-2.15, 57, limit=8)
#print "obs_list_near \n", obs_list_near, "\n"

obs = owm.weather_at_place('London,uk')                    # Toponym
#obs = owm.weather_at_id(2643741)                           # City ID
#obs = owm.weather_at_coords(-0.107331,51.503614)           # lat/lon

#print "time UNIX GMT", obs.get_reception_time()              # UNIX GMT time
#print "time ISO", obs.get_reception_time(timeformat='iso')   # ISO8601
#print "time/date", obs.get_reception_time(timeformat='date') # datetime.datetime instance

# getting the weather observations
w = obs.get_weather()
cloud = w.get_clouds()                                     # Get cloud coverage
rain = w.get_rain()                                       # Get rain volume
snow = w.get_snow()                                       # Get snow volume
wind = w.get_wind()                                       # Get wind degree and speed
humidity = w.get_humidity()                                   # Get humidity percentage
pressure = w.get_pressure()                                   # Get atmospheric pressure
temp = w.get_temperature()                                # Get temperature in Kelvin
tempC = w.get_temperature(unit='celsius')                  # ... or in Celsius degs
tempF = w.get_temperature('fahrenheit')                    # ... or in Fahrenheit degs
status = w.get_status()                                     # Get weather short status
detail_status = w.get_detailed_status()                           # Get detailed weather status
code = w.get_weather_code()                               # Get OWM weather condition code
icon = w.get_weather_icon_name()                          # Get weather-related icon name
sunrise = w.get_sunrise_time('iso')                               # Sunrise time (GMT UNIXtime or ISO 8601)
sunset = w.get_sunset_time('iso')                           # Sunset time (GMT UNIXtime or ISO 8601)

# metadata
l = obs.get_location()
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