import sys
from collections import deque
from math import sqrt, isnan

min_int = -sys.maxsize

class Node:

    def __init__(self, value, left_child=None, right_child=None, left_parent=None, right_parent=None):

        self.left_child = left_child
        self.right_child = right_child
        self.left_parent = left_parent
        self.right_parent = right_parent
        self.value = value
        self.printed = False

        if left_parent:
            self.left_parent.right_child = self
        
        if right_parent:
            self.right_parent.left_child = self

    def set_value(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def print_pyramid(self):
        if self.left_child:
            self.left_child.print_pyramid()
        if not self.printed:
            print(self.value)
            self.printed = True
        if self.right_child:
            self.right_child.print_pyramid()

def is_prime(n):
    if n < 2: 
        return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True

def create_node(value, left_parent=None, right_parent=None):
    
    global result, depth, q

    node = Node(value=value, left_parent=left_parent, right_parent=right_parent)

    if not isnan(value):
        if depth > result[0]:
            result = (depth, value)
        elif depth == result[0] and value > result[1]:
            result = (depth, value)


    q.append(node)
    return node


values = open('src.txt').read().split()
values.reverse()

depth = 0
result = (depth, min_int)

q = deque()
root_value = int(values.pop())
if is_prime(root_value):
    root_value = float('nan')
root = create_node(root_value)


while len(values) > 0:
    left_parent = None
    depth = depth + 1

    for j in range(depth):
        value = int(values.pop())
        right_parent = q.popleft()
        if is_prime(value):
            value = float('nan')
        elif not left_parent or isnan(left_parent.value) or right_parent > left_parent:
            value = value + right_parent.value
        else:
            value = value + left_parent.value
            
        create_node(value, left_parent, right_parent)
        left_parent = right_parent

    value = int(values.pop())

    if is_prime(value):
        value = float('nan')
    create_node(value+left_parent.value, left_parent)

print("maximum sum: ", result[1])
print("maximum depth: ", result[0])