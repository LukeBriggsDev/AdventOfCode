import os

class Cube:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)
        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)
        self.z1 = min(z1, z2)
        self.z2 = max(z1, z2)
    
    def get_positions(self):
        x = self.x1
        y = self.y1
        z = self.z1
        positions = set()
        while x <= self.x2 and x >= -50 and x <= 50:
            while y <= self.y2 and y >= -50 and y <= 50:
                while z <= self.z2 and z >= -50 and z <= 50:
                    positions.add((x, y, z))
                    z += 1
                y += 1
                z = self.z1
            x +=1
            y = self.y1
        return positions


if __name__ == "__main__":
    instructions = []
    with open(os.path.dirname(__file__) + "/input.txt") as f:
        for line in f:
            option, part_2 = line.split(' ')
            x, y, z = part_2.split(',')
            x1,x2 = x.split('..')
            y1,y2 = y.split('..')
            z1,z2 = z.split('..')
            instructions.append((option, Cube(int(x1[2:]), int(x2), int(y1[2:]), int(y2), int(z1[2:]), int(z2))))

    lit = set()
    length = len(instructions)
    count = 0
    for instruction in instructions:
        count += 1
        print(count,"/",length)
        if instruction[0] == 'on':
            lit = lit.union(instruction[1].get_positions())

        else:
            lit = lit - instruction[1].get_positions()

    print(len(lit))
        
