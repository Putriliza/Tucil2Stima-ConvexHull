import numpy as np

def orientation(p1, p2, p3):
    """
        prekondisi: p1, p2, dan p3 merupakan array yang terdefenisi, merepresentasikan titik
        proses: Menentukan posisi titik p3 terhadap garis p1p2 berdasarkan determinan
    """
    det = p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p3[0]*p2[1] - p2[0]*p1[1] - p1[0]*p3[1]
    if (np.allclose(det, 0)): det = 0.0
    
    if (det > 0): return 1          # left
    elif (det < 0): return -1       # right
    return 0                        # in line

def pointMax(sub, p1, p2):
    """
        prekondisi: array sub tidak kosong
                    p1 dan p2 merupakan array yang terdefenisi, merepresentasikan titik-titik
        proses: menentukan titik pada array sub yang memiliki jarak terjauh terhadap garis p1p2
                jika ada beberapa titik dengan jarak terjauh, akan terpilih yang pertama
    """
    max = 0.0
    pMax = np.array([])
    for p in sub:
        d = np.linalg.norm(np.cross(p2-p1, p1-p))/np.linalg.norm(p2-p1)
        if (d > max):
            max = d
            pMax = p

    return pMax

def addHull(sub, pBegin, pEnd):
    """
        prekondisi: array sub terdefenisim boleh kosong
                    pBegin dan pEnd merupakan array yang terdefenisi, merepresentasikan titik
                    dan merupakan convex hull yang sudah diketahui di sisi tersebut
        proses: menentukan convex hull pada suatu bagian, dilakukan secara rekursif
    """
    if len(sub) == 0:
        return np.empty((0,2), float)
    else:
        pMax = pointMax(sub, pBegin, pEnd)
        result = right = left = np.empty((0,2), float)
        
        for point in sub:
            if orientation(pBegin, pMax, point) == 1: left = np.append(left, [point], axis=0)
            elif orientation(pEnd, pMax, point) == -1: right = np.append(right, [point], axis=0)
            
        result = np.append(result, addHull(right, pMax, pEnd), axis=0)
        result = np.append(result, [pMax], axis=0)
        result = np.append(result, addHull(left, pBegin, pMax), axis=0)

        return result

def myConvexHull(points):
    """
        prekondisi: array points terdefenisi, minimal terdapat 2 titik
        proses: melakukan divide and conquer untuk menentukan convex hull keseluruhan
    """
    points = points[np.lexsort((points[:, 1], points[:, 0]))]
    p1 = points[0]
    pn = points[-1]
    result = right = left = np.empty((0,2), float)

    for point in points:
        if orientation(p1, pn, point) == 1: left = np.append(left, [point], axis=0)
        elif orientation(p1, pn, point) == -1: right = np.append(right, [point], axis=0)

    result = np.append(result, [p1], axis=0)
    result = np.append(result, addHull(right, pn, p1), axis=0)
    result = np.append(result, [pn], axis=0)
    result = np.append(result, addHull(left, p1, pn), axis=0)

    return result