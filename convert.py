"""
This file convert a list of points from the source file to 2 files
output_x.wav and output_y.wav.
"""

#/usr/bin/env python

import math as m
import numpy as np

src_file = "coorSuperposition.txt"
default_step = 2

dst_x = open("output_x.wav", "wb")
dst_y = open("output_y.wav", "wb")


def interm_points(x1, y1, x2, y2, step):
    """Return a regular list of points spaced by `step`"""

    dist = m.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return map(int, np.linspace(x1, x2, dist // step)), map(int, np.linspace(y1, y2, dist // step))


def convert_to_stereo_streams(filename=src_file):
    x_stream, y_stream = [], []

    with open(filename, 'r') as f:

        src_content = f.readlines()

        for line, next_line in zip(src_content, src_content[1:] + src_content[0]):

            x1, y1 = [int(i) for i in line.split(",")]
            x2, y2 = [int(i) for i in next_line.split(",")]

            x1 = - 128 * (x1 - 187) // 187 + 128
            y1 = - 128 * (150 - y1) // 150 + 128

            x2 = - 128 * (x2 - 187) // 187 + 128
            y2 = - 128 * (150 - y2) // 150 + 128

            # Add regular intermediate points
            l1, l2 = interm_points(x1, y1, x2, y2, default_step)
            x_stream.extend(l1)
            y_stream.extend(l2)

    return x_stream, y_stream

if __name__ == '__main__':

    x_bytes, y_bytes = convert_to_stereo_streams(src_file)
    # Write to output
    dst_x.write(bytes(x_bytes))
    dst_y.write(bytes(y_bytes))
