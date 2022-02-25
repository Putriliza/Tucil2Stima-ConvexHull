import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as pth

# posisi p3 terhadap p1->p2
def orientation(p1, p2, p3):
    matrix = np.array([p1, p2, p3])
    matrix = np.column_stack((matrix, np.ones((3,1))))
    det = np.linalg.det(matrix)
    if (np.allclose(det, 0)): det = 0.0
    # det = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p3[0]*p2[1] - p2[0]*p1[1] - p1[0]*p3[1]
    print(f"{p1}, {p2}, {p3}, {det}")
    if (det > 0): return 1          # left
    elif (det < 0): return -1       # right
    return 0                        # in line

def pointMax(p1, p2, sub):
    max = 0.0
    pMax = np.array([])
    for p in sub:
        d = np.linalg.norm(np.cross(p2-p1, p1-p))/np.linalg.norm(p2-p1)
        if (d > max):
            max = d
            pMax = p
    print(f"sub = {sub}, pmax={pMax}, p1={p1}, p2{p2}")
    return pMax

def inTriangle(p1, p2, p3, p4):
    triangle = pth.Path(np.array([p1, p2, p3], dtype=object))
    return triangle.contains_point(p4)


def addHull(sub, pBegin, pEnd):
    if len(sub) == 0: return np.empty((0,2), float)
    else:
        pMax = pointMax(pBegin, pEnd, sub)
        # for point in sub:
        #     if inTriangle(pBegin, pEnd, pMax, point): 
        #         sub.remove(point)
        left = np.empty((0,2), float)
        right = np.empty((0,2), float)
        result = np.empty((0,2), float)
        
        for point in sub:
            print(f"point = {point}")
            if orientation(pBegin, pMax, point) == 1: left = np.append(left, [point], axis=0)
            elif orientation(pEnd, pMax, point) == -1: right = np.append(right, [point], axis=0)
        print(f"left = {left}")
        print(f"right = {right}")
        print("-----------------------------------------------------\n")
            
        result = np.append(result, addHull(right, pMax, pEnd), axis=0)
        result = np.append(result, [pMax], axis=0)
        result = np.append(result, addHull(left, pBegin, pMax), axis=0)

        return result

def myConvexHull(points):
    points = points[np.lexsort((points[:, 1], points[:, 0]))]
    p1 = points[0]
    pn = points[-1]

    result = np.empty((0,2), float)
    left = np.empty((0,2), float)
    right = np.empty((0,2), float)

    for point in points:
        if orientation(p1, pn, point) == 1: left = np.append(left, [point], axis=0)
        elif orientation(p1, pn, point) == -1: right = np.append(right, [point], axis=0)

    result = np.append(result, [p1], axis=0)
    result = np.append(result, addHull(right, pn, p1), axis=0)
    result = np.append(result, [pn], axis=0)
    result = np.append(result, addHull(left, p1, pn), axis=0)

    return result