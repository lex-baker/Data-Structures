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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# Comments are for worst case
nums = []
# 9072 accesses
for text in texts:
    # nums starts at 0 and ends at 9072
    if text[0] not in nums:
        nums += [ text[0] ]
    # nums starts at 0 and ends at 9072
    if text[1] not in nums:
        nums += [ text[1] ]
    # O(N(N + N))

# 5213 accesses
for call in calls:
    # nums starts at 9072 and ends at 14,285
    if call[0] not in nums:
        nums += [ call[0] ]
    # nums starts at 9072 and ends at 14,285
    if call[1] not in nums:
        nums += [ call[1] ]
    # O(N(N + N))  
      

amountOfNums = len(nums)
print(f"There are {amountOfNums} different telephone numbers in the records.")