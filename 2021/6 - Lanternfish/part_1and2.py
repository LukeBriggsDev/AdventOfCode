"""
--- Part Two ---

Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!

How many lanternfish would there be after 256 days?
"""

import os
from collections import Counter

def fish_count(input_file, days):
    fish = {0:0, 1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    with open(input_file) as f:
        for group in Counter([int(x) for x in f.read().split(",")]).items():
            fish[group[0]] += group[1]

    for i in range(days):
        new_borns = 0
        resets = 0
        for group in fish:
            if group == 0:
                new_borns = fish[0]
                resets = fish[0]
                fish[0] = 0
            else:
                fish[group-1] += fish[group]
                fish[group] = 0
        fish[8] = new_borns
        fish[6] += resets
    return sum(fish.values())


if __name__ == "__main__":
    print(fish_count(os.path.dirname(__file__) + "/input.txt", 256))

    

