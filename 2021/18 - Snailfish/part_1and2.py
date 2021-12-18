import os
from math import ceil
from copy import deepcopy
import sys
import itertools

class Node:
    def __init__(self, parent, nested_list):
        try:
            self.left = Node(self, nested_list[0]) 
        except TypeError:
            self.left = None
        try:
            self.right = Node(self, nested_list[1])
        except TypeError:
            self.right = None

        self.parent = parent
        self.value = nested_list
    
    def as_list(self):
        if type(self.value) is int:
            return self.value
        else:
            return [self.left.as_list(), self.right.as_list()]
    def explode(self, level=0, finished=[False]):
        if finished[0]:
            return
        if level == 4 and type(self.value) is list:
            left, right = self.left.value, self.right.value
            #add to left
            node = self
            while node.parent.left is node:
                node = node.parent
                if node.parent is None:
                    break
            if node.parent is not None:
                node = node.parent.left
                while node.right is not None:
                    node = node.right
                node.value += left
            #add to right
            node = self
            while node.parent.right is node:
                node = node.parent
                if node.parent is None:
                    break
            if node.parent is not None:
                node = node.parent.right
                while node.left is not None:
                    node = node.left
                node.value += right
            self.value = 0
            self.left = None
            self.right = None
            finished[0] = True
        else:
            if self.left:
                self.left.explode(level=level+1, finished=finished)
            if self.right:
                self.right.explode(level=level+1, finished=finished)

    def split(self, finished=[False]):
        if finished[0]:
            return
        if self.left:
            self.left.split(finished=finished)
        if self.right:
            self.right.split(finished=finished)
        
        if self.left is None and self.right is None:
            if self.value > 9:
                left = Node(self, self.value//2)
                right = Node(self, ceil(self.value/2))
                self.left = left
                self.right = right
                self.value = [left, right]
                finished[0] = True

    def get_sum(self):
        if type(self.value) is int:
            return self.value
        else:
            return self.left.get_sum() * 3 + self.right.get_sum() * 2

def add(num_1, num_2):
    return [num_1, num_2]

def reduce_list(num):
    tree = Node(None, num)
    last_tree = Node(None,0)
    while tree.as_list() != last_tree.as_list():
        last_tree = deepcopy(tree)
        tree.explode(finished=[False])
        if tree.as_list() == last_tree.as_list():
            tree.split(finished=[False])
    return tree.as_list()


if __name__ == "__main__":
    with open(os.path.dirname(__file__)+"/input.txt") as f:
        numbers = [eval(x) for x in f.read().split("\n")]

    total = numbers[0]
    for i in range(1, len(numbers)):
        total = reduce_list(add(total, numbers[i]))


    print("PART1: ",Node(None, total).get_sum())

    # Part 2
    perms = itertools.permutations(numbers, 2)
    max_total = 0
    for perm in perms:
        mag = Node(None, reduce_list(add(perm[0], perm[1]))).get_sum()
        if mag > max_total:
            max_total = mag
    print("PART2:", max_total)