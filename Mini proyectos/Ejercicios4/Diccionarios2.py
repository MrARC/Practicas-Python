"""
Nested Dictionaries and Lists
Tou may find you need dictionaries and lists that contain other dictionaries and lists.
Lists are useful to contain an ordered series of values, and dictionaries are useful for
associating keys with values. For example, here’s a program that uses a dictionary that contains
other dictionaries in order to see who is bringing what to a picnic. The totalBrought() function
can read this data structure and calculate the total number of an item being brought by all the guests.

https://automatetheboringstuff.com/chapter5/

"""

allGuests = {
    "Alice": {"apples": 5, "pretzels": 12},
    "Bob": {"ham sandwiches": 3, "apples": 2},
    "Carol": {"cups": 3, "apple pies": 1},
}


def totalBrought(guests: dict, item: str):
    total = 0
    for k, v in guests.items():
        total += v.get(item, 0)
    return total


print("Number of things being brought:")
print(" - Apples         " + str(totalBrought(allGuests, "apples")))
print(" - Cups           " + str(totalBrought(allGuests, "cups")))
print(" - Cakes          " + str(totalBrought(allGuests, "cakes")))
print(" - Ham Sandwiches " + str(totalBrought(allGuests, "ham sandwiches")))
print(" - Apple Pies     " + str(totalBrought(allGuests, "apple pies")))