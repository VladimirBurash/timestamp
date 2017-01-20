#!/usr/bin/python
import sys,ntplib,datetime
client = ntplib.NTPClient()
response = client.request('pool.ntp.org')
correct_time = response.tx_time
timestamp = sys.argv[1]
res = abs(int(timestamp)-correct_time)
if res < 10:
    print("Time is correct")
    sys.exit(0)
else:
    print("Time is incorrect")
    sys.exit(1)
