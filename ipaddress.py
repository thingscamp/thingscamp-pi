import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

# print (get_ip_address('wlan0'))
my_IP = get_ip_address('wlan0')

from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("IP address is %s" % my_IP) 

