import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from MyConvexHull import myConvexHull

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
