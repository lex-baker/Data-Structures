"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possibles = {}
# Finding all numbers that made outgoing calls
# N accesses
for call in calls:
    # N accesses
    if call[0] not in possibles.keys():
        possibles[ call[0] ] = None

# Removing the numbers that received at least one call
# N accesses
for call in calls:
    # N accesses
    possibles.pop(call[1], None)

# Removing the numbers that sent or received at least one text
# N accesses
for text in texts:
    # N accesses
    possibles.pop(text[0], None)
    # N accesses
    possibles.pop(text[1], None)

print("These numbers could be telemarketers: ")
# N log N accesses
possibles = sorted(list(possibles.keys()))
for possible in possibles:
    print(possible)