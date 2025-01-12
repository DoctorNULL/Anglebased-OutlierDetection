from matplotlib.pyplot import scatter, show, legend
import numpy as np
from math import pi
from random import normalvariate


def calAngle(p1: tuple, p2: tuple, p3: tuple) -> float:
    v1 = np.subtract(np.array(p1), np.array(p2))
    v2 = np.subtract(np.array(p1), np.array(p3))
    product = np.dot(v1, v2)
    v1Norm = np.linalg.norm(v1)
    v2Norm = np.linalg.norm(v2)

    return np.arccos(product / (v1Norm * v2Norm)) * 180 / pi


def getAllAngles(p: tuple, points: list) -> list:
    res = []

    ps = [x for x in points if x != p]

    allPairs = [(a, b) for iden, a in enumerate(ps) for b in ps[iden + 1:]]

    for pair in allPairs:
        res.append(calAngle(p, pair[0], pair[1]))

    return res


def calVariance(angles: list) -> float:
    a = [x * pi / 180 for x in angles]
    m = sum(a) / len(a)
    v = [(x - m) ** 2 for x in a]
    return sum(v) / len(v)


# points = [(1, 1), (2, 2), (3, 3), (1, 5), (5, 1), (3, 2), (1,3), (2, 3), (4, 1), (10, 15), (20, 10)]

points = []
for i in range(100):
    points.append((normalvariate(5, 3), normalvariate(10, 5)))

for i in range(10):
    points.append((normalvariate(50, 50), normalvariate(50, 50)))

normal = []
outlier = []

for p in points:

    #    print("Point : ", p)
    ang = getAllAngles(p, points)

    #    print("Angles : ", ang)

    var = calVariance(ang)

    if var < 0.3:
        outlier.append(p)
        print("Variance : ", var)
        print(f"Point {p} is an Outlier")
        print("\n--------------------------\n")
    else:
        normal.append(p)

normalXs = [x[0] for x in normal]
outXs = [x[0] for x in outlier]
normalYs = [x[1] for x in normal]
outYs = [x[1] for x in outlier]

scatter(normalXs, normalYs, color="blue", label="Normal")
scatter(outXs, outYs, color="red", label="Outlier")
legend()
show()
