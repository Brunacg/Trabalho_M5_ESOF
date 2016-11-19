import random
import rstr
import datetime

def gen_timestamp():
	year = random.randint (1915, 2015)
	month = random.randint(1,12)
	day = random.randint (1,30)
	hour = random.randint (1,23)
	minute = random.randint (1, 59)
	second = randon.randint(1,59)
	microsecond = random.randint (1, 999999) 
	date = datetime.datetime (year, month, day, hour, minute, second, microsecond).isoformat (" ")
	return date

gen_timestamp()

