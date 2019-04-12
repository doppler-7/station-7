#!/usr/bin/env python3
"""great-circle initial bearing from A to B. i kept running it both ways and getting
the same line, which is the whole problem with a line. usage: bearing.py lat1 lon1 lat2 lon2"""
import sys, math

def bearing(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dl = math.radians(lon2 - lon1)
    y = math.sin(dl) * math.cos(p2)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    return (math.degrees(math.atan2(y, x)) + 360) % 360

if __name__ == "__main__":
    a = list(map(float, sys.argv[1:5]))
    print(f"{bearing(*a):.1f}")
