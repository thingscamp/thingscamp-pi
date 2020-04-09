import codebug_i2c_tether

import datetime

import time

# make a connection with CodeBug

cb = codebug_i2c_tether.CodeBug()

cb.open()

# function for scrolling messages on CodeBug’s display

def scroll_message(message):

    length = len(message)

    for i in range(0,length*-5,-1):

        cb.write_text(i, 0, message, direction="right")

        time.sleep(.15)

while True:

    # get the time and scroll it

    time_str = datetime.datetime.now().strftime("%H:%M:%S")

    scroll_message(" Time " + time_str)

    # get the date and scroll it

    date_str = datetime.datetime.now().strftime("%d/%m/%Y")

    scroll_message(" Date " + date_str)
