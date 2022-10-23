# d = {key: [value, previous, next]}
d = {}

#latest = d[some_key]
latest = None

def set(key, value):
    global latest
    if key in d:
        prev = d[key][1]
        next = d[key][2]
        if next != None:
            # the last element is NOT being changed, meaning everything must be modified in some way
            if prev == None:
                # if key being set is the first
                d[next][1] = None
            else:
                #if key being set is not the first
                d[next][1] = prev
                # if key being set is not the last
                d[prev][2] = next
            d[key][1] = latest
            d[key][2] = None
            d[latest][2] = key
            latest = key
        d[key][0] = value
    
    else:
        if latest == None:
            # first key assigned to dictionary
            d[key] = [value, None, None]
            latest = key
        else:
            d[key] = [value, latest, None]
            d[latest][2] = key
            latest = key
    print(d)


def get(key):
    global latest
    if key in d:
        prev = d[key][1]
        next = d[key][2]
        if next != None:
            # the last element is NOT being changed, meaning everything must be modified in some way
            if prev == None:
                # if key being set is the first
                d[next][1] = None
            else:
                #if key being set is not the first
                d[next][1] = prev
                # if key being set is not the last
                d[prev][2] = next
            d[key][1] = latest
            d[key][2] = None
            d[latest][2] = key
            latest = key
        return d[key][0]
    else:
        return -1

def remove_first():
    global latest
    first = latest
    while d[first][1] != None:
        first = d[first][1]
    # setting first's next value's previous to None
    d[d[first][2]][1] = None
    d.pop(first)
    print(d)


# set("first", "one")
# set("second", "two")
# set("third", "three")
# set("third", "alt_three")


set("first", "one")
set("second", "two")
set("third", "three")
print("\n")
print(get("first"))
print(d)
print()
set("first", "alt_one")
print()
print(get("first"))
print(d)
print()
set("fourth", "four")
print()
remove_first() #should remove second
remove_first() #should remove third












# # ld = {'first': ld['second'], 'second': ld['third'], 'third': None}
# d = {}
# d[1] = None
# d[2] = None
# d[1] = d[2]
# d[3] = None
# d[2] = d[3]
# print(d[1])
# #getting 2
# s = set()
# s += 1
# print(s)

# arr = []
# arr.append(1)
# arr.append(2)
# arr.append(3)
# arr.append(4)
# arr.


