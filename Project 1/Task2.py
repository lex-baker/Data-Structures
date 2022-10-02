"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def findMaxNum(times):
    maxValue = max(times.values())
    # N accesses
    for key in times.keys():
        if(times[key] == maxValue):
            return key, maxValue

times = {}
# N accesses
for call in calls:
    # N access
    if call[0] not in times:
        times[call[0]] = int(call[3])
    else:
        times[call[0]] += int(call[3])

    # N accesses
    if call[1] not in times:
        times[call[1]] = int(call[3])
    else:
        times[call[1]] += int(call[3])

num, time = findMaxNum(times)
print(f'{num} spent the longest time, {time} seconds, on the phone during September 2016.')