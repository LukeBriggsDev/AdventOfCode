import os
import itertools
import numpy as np
import scipy.spatial.transform.rotation as R

def rotated_vectors(vec, axis, rotation_degrees):

    rotation_radians = np.radians(rotation_degrees)
    rotation_vector = rotation_radians * axis
    rotation = R.Rotation.from_rotvec(rotation_vector)
    rotated_vec = rotation.apply(vec)
    return [int(x) for x in rotated_vec]


class Beacon():
    def __init__(self, x, y, z, scanner):
        self.scanner = scanner
        self.x = x
        self.y = y
        self.z = z
        self.beacon_vectors = []

    def add_beacon(self, beacon):
        self.beacon_vectors.append([beacon.x - self.x,beacon.y-self.y,beacon.z - self.z])

    def __repr__(self):
        string = f"Beacon(x: {self.x}, y: {self.y}, z: {self.z}, Scanner: {scanner.id})"
        return string

class Scanner:
    def __init__(self, id):
        self.id = id
        self.x = 0
        self.y = 0
        self.z = 0
        self.beacons = []

    def add_beacon(self, beacon):
        self.beacons.append(beacon)

if __name__ == "__main__":
    scanners = []
    with open(os.path.dirname(__file__) + "/test.txt") as f:
        scanner = Scanner(0)
        scanner_count = 0
        for line in f:
            if line.startswith('---'):
                continue
            elif line == '\n':
                scanners.append(scanner)
                scanner_count += 1
                scanner = Scanner(scanner_count)
            else:
                coords = [int(x) for x in line.strip().split(',')]
                beacon = Beacon(*coords, scanner)
                scanner.add_beacon(beacon)
        scanners.append(scanner)

    for scanner in scanners:
        for beacon1 in scanner.beacons:
            for beacon2 in scanner.beacons:
                if beacon1 is not beacon2:
                    beacon1.add_beacon(beacon2)

    axes = np.array([[1, 1, 1],[1, 1, 0],[1, 0, 1],[1, 0, 0],[0, 1, 1],[0, 1, 0],[0, 0, 1],[0, 0, 0]])

    scanner = scanners[0]
    total_len = len(scanner.beacons)
    match_list = {}
    count = 0
    for beacon in scanner.beacons:
        count += 1
        print(f"{count}/{total_len}")
        for vector in beacon.beacon_vectors:
            # Find corresponding vector
            for co_scanner in scanners[1:]:
                for co_beacon in co_scanner.beacons:                     
                    for axis in axes:
                        for degrees in [90, 180, 270]:
                            matches = 0
                            for co_vector in co_beacon.beacon_vectors:
                                rotated_vector = rotated_vectors(co_vector, axis, degrees)
                                if vector == rotated_vector:
                                    key = (co_scanner.id, degrees, tuple(axis))
                                    try:
                                        match_list[key] += 1
                                    except KeyError:
                                        match_list[key] = 1

    print(match_list)