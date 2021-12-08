"""
--- Part Two ---

Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?
"""
import os
def count_uniques(input_file):
    entries = []
    with open(input_file) as f:
        for line in f:
            signal_pattern = tuple([digit for digit in line.strip().split(" | ")[0].split(' ')])
            output_value = tuple([digit for digit in line.strip().split(" | ")[1].split(' ')])
            entries.append((signal_pattern, output_value))

    display = [0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010, 0b1101011, 0b1101111, 0b1010010, 0b1111111, 0b1111011]
    decoded_outputs = []
    for entry in entries:
        decoded_output = []
        encoded_patterns = get_digit_encodes(entry[0])
        for digit in entry[1]:
            for i in range(10):
                if binary_encode_digit(digit) == encoded_patterns[i]:
                    decoded_output.append(str(i))
        decoded_outputs.append(decoded_output)

    return sum([int(''.join(x)) for x in decoded_outputs])

        
def binary_encode_digit(digit):
    letters = "abcdefg"
    binary = ['0','0','0','0','0','0','0']
    for letter in digit:
        binary[ord(letter)-97] = '1'
    return int(''.join(binary),base=2)

def get_digit_encodes(signal_patterns):
    encoded_patterns = {0:None,1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None,8:None,9:None}
    encode = {"a":None,"b":None,"c":None,"d":None,"e":None,"f":None,"g":None,}

    # Match certain patterns
    for digit in signal_patterns:
        if len(digit) == 2:
            encoded_patterns[1] = binary_encode_digit(digit)
        elif len(digit) == 4:
            encoded_patterns[4] = binary_encode_digit(digit)
        elif len(digit) == 3:
            encoded_patterns[7] = binary_encode_digit(digit)
        elif len(digit) == 7:
            encoded_patterns[8] = binary_encode_digit(digit)
    encode["a"] = encoded_patterns[7] ^ encoded_patterns[1]
    # 9 = 9 ^ (4 | a) with 1 bit left over
    for digit in signal_patterns:
        if len(digit) == 6 and \
            bin(binary_encode_digit(digit) ^ 
            (encoded_patterns[4] | encode["a"])).count("1") == 1:
            encoded_patterns[9] = binary_encode_digit(digit)
    encode['g'] = encoded_patterns[9] ^ (encoded_patterns[4] | encode['a'])
    encode['e'] = encoded_patterns[9] ^ encoded_patterns[8]
    # 3 = 7 | g  with 1 bit left over
    for digit in signal_patterns:
        if len(digit) == 5 and \
            bin(binary_encode_digit(digit) ^ 
            (encoded_patterns[7] | encode["g"])).count("1") == 1:
            encoded_patterns[3] = binary_encode_digit(digit)
    encode['d'] = (encoded_patterns[3] ^ encoded_patterns[7]) ^ encode['g']
    encode['b'] = (encoded_patterns[9] ^ encoded_patterns[3])
    # 6 = len == 6 and ^ (a|b|d|e|g) leaves 1 bit
    for digit in signal_patterns:
        if len(digit) == 6 and \
            bin(binary_encode_digit(digit) ^ 
            (encode['a'] | encode['b'] | encode['d'] | encode['e'] | encode["g"])).count("1") == 1:
            encoded_patterns[6] = binary_encode_digit(digit)
    encode['c'] = encoded_patterns[8] ^ encoded_patterns[6]
    encode['f'] = encoded_patterns[1] ^ encode['c']

    encoded_patterns[0] = encoded_patterns[8] ^ encode['d']
    encoded_patterns[2] = (encoded_patterns[3] ^ encode['f']) | encode['e']
    encoded_patterns[5] = encoded_patterns[6] ^ encode['e']

    return encoded_patterns


    


if __name__ == "__main__":
    print(count_uniques(os.path.dirname(__file__)+"/input.txt"))