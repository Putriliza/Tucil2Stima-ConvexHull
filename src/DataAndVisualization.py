import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from MyConvexHull import myConvexHull

def loadData(opt):
    """
        prekondisi: opt merupakan nilai yang valid untuk merefer dataset (0-3)
        proses: meload data yang sesuai
                menginput pilihan atribut dari user
                menampilkan visualisasi jika valid
    """
    dsNames = ["IRIS", "WINE", "BREAST_CANCER", "DIGITS"]
    dataset = [datasets.load_iris(), datasets.load_wine(), datasets.load_breast_cancer(), datasets.load_digits()] 
    data = dataset[opt-1]

    print(f"\nAvailable atributs: ")
    for i in range(len(data.feature_names)):
        print(f"{i+1}. {data.feature_names[i]}")
    print(f"\nChoose atribut (x and y): ")
    x = int(input("x: ")) - 1
    y = int(input("y: ")) - 1

    maxCol = len(data.feature_names) - 1
    if (x < 0 or x > maxCol or y < 0 or y > maxCol):
        print("The choosen atribut is invalid")
    else:
        visualization(data, x, y, dsNames[opt-1])

def visualization(data, x, y, dsName):
    """
        prekondisi: data terdefinisi untuk suatu dataset dsName, x dan y indeks atribut data yang valid
        proses: membentuk dataframe
                menentukan convex hull dari data dengan myConvexhull()
                menampilkan visualisasi
                menyimpan visualisasi jika diinginkan user
    """
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)

    plt.figure(figsize = (10, 6))
    colors = ['b','orange','g','r', 'purple', 'brown', 'pink', 'gray', 'y', 'cyan']
    title = f"{data.feature_names[x].upper()} vs {data.feature_names[y].upper()} ({dsName})"
    plt.title(title)
    plt.xlabel(data.feature_names[x])
    plt.ylabel(data.feature_names[y])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[x, y]].values
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        hull = myConvexHull(bucket)
        # print(hull)
        plt.plot(np.append(hull[:, 0], hull[0, 0]), np.append(hull[:, 1], hull[0, 1]), colors[i])
    plt.legend()

    save = input("\nSave image (y/n)? ")
    if (save == 'y'):
        plt.savefig('../test/' + title + '.png')
    plt.show()
