# Use random & datetime in script.

''' "Random OTP Generator with Timestamp"'''

import random
import datetime

# Generate OTP
otp = random.randint(100000, 999999)

# Current date and time
current_time = datetime.datetime.now()

# Expiry time (2 minutes after current time)
expiry_time = current_time + datetime.timedelta(minutes=2)

# Print outputs
print("Your OTP is:", otp)
print("OTP Generated Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
print("OTP Expiry Time   :", expiry_time.strftime("%Y-%m-%d %H:%M:%S"))

# . Create math_utils module & import

import math_utils

print ("addition", math_utils.add(5,3))
print ("subtraction", math_utils.subtract(11,2))
print ("multiplication ", math_utils.multiply(7,5))
print (" division" , math_utils.divide(6,3))

