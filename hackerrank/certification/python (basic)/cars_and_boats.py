#!/bin/python3

import math
import os
import random
import re
import sys


class Vehicle:
    def __init__(self, max_speed, units):
        self.max_speed = max_speed
        self.units = units

    def __str__(self):
        return "{} with the maximum speed of {} {}".format(
            self.__class__.__name__, self.max_speed, self.units)


class Car(Vehicle):
    def __init__(self, max_speed, units):
        super().__init__(max_speed, units)


class Boat(Vehicle):
    def __init__(self, max_speed):
        super().__init__(max_speed, "knots")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
