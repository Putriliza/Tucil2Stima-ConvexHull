from Visualization import *
from sklearn import datasets

def loadData(opt):
    """
        prekondisi: opt memiliki nilai yang valid untuk refer ke dataset (1-4)
        proses: meload data yang sesuai
                menginput pilihan attribute dari user
                memanggil fungsi visualisasi jika valid
    """
    dsNames = ["IRIS", "WINE", "BREAST_CANCER", "DIGITS"]
    if (opt == 1): data = datasets.load_iris()
    elif (opt == 2): data = datasets.load_wine()
    elif (opt == 3): data = datasets.load_breast_cancer()
    elif (opt == 4): data = datasets.load_digits()

    print(f"\nAvailable attributes: ")
    for i in range(len(data.feature_names)):
        print(f"{i+1}. {data.feature_names[i]}")
    print(f"\nChoose attribute (x and y): ")
    x = int(input("x: ")) - 1
    y = int(input("y: ")) - 1

    maxCol = len(data.feature_names) - 1
    if (x < 0 or x > maxCol or y < 0 or y > maxCol):
        print("The choosen attribute is invalid")
    else:
        visualization(data, x, y, dsNames[opt-1])



# ---------------------------- PROGRAM UTAMA --------------------------------

print("===================LINEAR SEPARABILITY TEST===================")

isRun = True
while (isRun):
    print("\n1. Iris")
    print("2. Wine")
    print("3. Breast_cancer")
    print("4. Digits")
    opt = int(input("Choose dataset: "))
    if (opt > 0 and opt <= 4):
        loadData(opt)
    else:
        print("Dataset not available")
    
    run = input("\nTry another test (y/n)? ")
    isRun = True if run == 'y' else False