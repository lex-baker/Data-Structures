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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# Two array accesses
firstText = texts[0]
lastCall = calls[-1]

# Three plus four array accesses
print(f'First record of texts, {firstText[0]} texts {firstText[1]} at time {firstText[2]}')
print(f'Last record of calls, {lastCall[0]} calls {lastCall[1]} at time {lastCall[2]}, lasting {lastCall[3]} seconds')