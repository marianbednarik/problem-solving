"""

Say you have a function that generates random numbers from 0 to 1. Estimate the constant Pi using this function.

"""
import math
import random

TOTAL_POINTS = 10000
RADIUS = 1


def estimate_pi():
    in_radius = 0
    for _ in range(TOTAL_POINTS):
        x = random.uniform(0, RADIUS)
        y = random.uniform(0, RADIUS)
        if math.sqrt(x ** 2 + y ** 2) < RADIUS:
            in_radius += 1
    return (in_radius * (RADIUS * 2) ** 2) / (TOTAL_POINTS * (RADIUS ** 2))


print(estimate_pi())
