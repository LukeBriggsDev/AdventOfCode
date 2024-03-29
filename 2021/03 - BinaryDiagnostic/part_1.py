"""
--- Day 3: Binary Diagnostic ---

The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, 
can tell you many useful things about the conditions of the submarine. 
The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). 
The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. 
For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, 
the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, 
then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
"""

import os
import math
def get_power_consumption(input_file):
    with open(input_file) as f:
        bytes = [line.strip() for line in f.readlines()]
    gamma_rate = get_most_common_bits(bytes)
    epsilon_rate = get_least_common_bits(bytes)

    return gamma_rate * epsilon_rate
                

def get_most_common_bits(input_arr):
    byte_length = get_byte_length(input_arr)
    line_count = 0
    bit_counts = [0 for i in range(byte_length)]
    gamma_rate = ['' for _ in bit_counts]
    for line in input_arr:
        line_count += 1
        for i in range(len(line)):
            bit_counts[i] += int(line[i])
    
    for i in range(len(bit_counts)):
        if bit_counts[i] >= line_count / 2:
            gamma_rate[i] = '1'
        else:
            gamma_rate[i] = '0'
    return int(''.join(gamma_rate), base=2)

def get_least_common_bits(input_arr):
    byte_length = get_byte_length(input_arr)
    most_common_bits = get_most_common_bits(input_arr)
    max_val = int('1' * byte_length, base=2)
    least_common_bits = most_common_bits ^ max_val
    return least_common_bits

def get_byte_length(input_arr):
        byte_length = len(input_arr[0])
        return byte_length

if "__main__" == __name__:
    print(get_power_consumption(os.path.dirname(__file__) + "/input.txt"))


