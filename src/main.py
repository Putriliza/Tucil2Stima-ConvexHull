from traceback import print_tb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from scipy.spatial import ConvexHull 
from ConvexHull import myConvexHull

def loadData(pil):
    dsNames = ["IRIS", "WINE", "BREAST_CANCER", "DIGITS"]
    dataset = [datasets.load_iris(), datasets.load_wine(), datasets.load_breast_cancer(), datasets.load_digits()] 
    data = dataset[pil-1]

    print(f"Atribut yang tersedia: ")
    for i in range(len(data.feature_names)):
        print(f"{i+1}. {data.feature_names[i]}")
    print(f"Pilih atribut (x dan y): ")
    x = int(input("x: ")) - 1
    y = int(input("y: ")) - 1

    maxCol = len(data.feature_names) - 1
    if (x < 0 or x > maxCol or y < 0 or y > maxCol):
        print("Atribut tidak valid")
    else:
        visualization(data, x, y, dsNames[pil-1])

def visualization(data, x, y, dsName):
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)

    plt.figure(figsize = (10, 6))
    colors = ['b','orange','g','r', 'purple', 'brown', 'pink', 'gray', 'y', 'cyan']
    plt.title(f"{data.feature_names[x]} vs {data.feature_names[y]} ({dsName})")
    plt.xlabel(data.feature_names[x])
    plt.ylabel(data.feature_names[y])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[x, y]].values
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        hull = myConvexHull(bucket)
        plt.plot(np.append(hull[:, 0], hull[0, 0]), np.append(hull[:, 1], hull[0, 1]), colors[i])
    plt.legend()
    plt.show()


print("""1. Iris
2. Wine
3. Breast_cancer
4. Digits""")
pil = int(input("Pilih dataset: "))
if (pil > 0 and pil <= 4):
    loadData(pil)
else:
    print("Dataset tidak tersedia")