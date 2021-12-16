import os
import math
import operator

class Packet:
    operators = [sum, math.prod, min, max, None, operator.gt, operator.lt, operator.eq]
    def __init__(self, start_pos, outer_packet):
        self.start_pos = start_pos
        self.outer_packet = outer_packet
        self.inner_packets = []
        self.packet_version = ""
        self.packet_ID = ""
        self.value = ""
        self.operator = None
        self.is_operator = False

    def get_version_sum(self):
        sum = 0
        for packet in self.inner_packets:
            sum += packet.get_version_sum()
        sum += int(self.packet_version, base=2)
        return sum

    def get_value(self):
        if not self.is_operator:
            return int(self.value, base=2)
        try:
            return self.operator([packet.get_value() for packet in self.inner_packets])
        except TypeError:
            return self.operator(*[packet.get_value() for packet in self.inner_packets])

    def read_packet(self, binary): # Return end_pos
        for i in range(self.start_pos, self.start_pos+3):
            self.packet_version += binary[i]
        for i in range(self.start_pos+3, self.start_pos+6):
            self.packet_ID += binary[i]

        if int(self.packet_ID, base=2) == 4:
            # Value packet
            finished = False
            end_pos = self.start_pos+6
            while not finished:
                if binary[end_pos] == "0":
                    finished = True
                self.value += binary[end_pos+1:end_pos+5]
                end_pos += 5

        else:
            # Operator packet
            type = int(self.packet_ID, base=2)
            self.is_operator = True
            self.operator = self.operators[type]

            if binary[self.start_pos + 6] == '0': # next 15 bits contain total length of sub-packets
                packet_length = int(binary[self.start_pos+7:self.start_pos+22], base=2)
                end_pos = self.start_pos + 22
                while end_pos < self.start_pos+22+packet_length:
                    new_packet = Packet(end_pos, self)
                    self.inner_packets.append(new_packet)
                    end_pos = new_packet.read_packet(binary)
                return end_pos
            else: # Next 11 bits contain number of sub-packets
                no_packets = int(binary[self.start_pos+7:self.start_pos+18], base=2)
                end_pos = self.start_pos + 18
                while len(self.inner_packets) < no_packets:
                    new_packet = Packet(end_pos, self)
                    self.inner_packets.append(new_packet)
                    end_pos = new_packet.read_packet(binary)
        
        return end_pos

if __name__ ==  "__main__":
    binary = ""
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        for line in f:
            for char in line.strip():
                binary += bin(int(char, base=16))[2:].zfill(4)

    parent_packet = Packet(0, None)
    parent_packet.read_packet(binary)
    print("Part 1:", parent_packet.get_version_sum())
    print("Part 2:", parent_packet.get_value())