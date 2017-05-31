#!/usr/bin/python
from datetime import datetime
now = datetime.now()
print("\033[1;42m%s/%s/%s | %s:%s:%s\033[1;m") % (now.day, now.month, now.year, now.hour, now.minute, now.second)


# By default, the script outputs the day before the month. Feel free to change this.
