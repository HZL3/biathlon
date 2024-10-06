from random import randint
# def splash ():
# open = 0
# closed = 1
open   = 0
closed = 1
a = open
b = closed
def is_open(value):
    return value == open
def is_closed(value):
    return value == closed

def new_targets():
    return [open]*5
# print (new_targets())

def close_target(targets, position):
    targets[position] = closed
    return targets
ts = new_targets()

def points(targets):
    n = 0
    for target in targets:
        if is_closed(target):
            n += 1
    return n
# def targets_to_string(targets):
def random_hit():
    return randint(0, 1) == 1
def shoot(targets, position):