import math
from itertools import product


def calculate_distance(w, h1, h2):
    return math.sqrt(w ** 2 + (h1 - h2) ** 2)


def max_cable_length(w, heights):
    N = len(heights)
    max_length = 0


    for combo in product(*[range(1, h + 1) for h in heights]):
        length = 0
        for i in range(N - 1):
            h1_top = combo[i]
            h1_bottom = 1
            h2_top = combo[i + 1]
            h2_bottom = 1


            lengths = [
                calculate_distance(w, h1_top, h2_top),
                calculate_distance(w, h1_top, h2_bottom),
                calculate_distance(w, h1_bottom, h2_top),
                calculate_distance(w, h1_bottom, h2_bottom)
            ]

            
            length += max(lengths)

        max_length = max(max_length, length)

    return max_length
