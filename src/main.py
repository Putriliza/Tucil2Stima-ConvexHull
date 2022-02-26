from DataAndVisualization import *

print("LINEAR SEPARABILITY TEST")

print("""1. Iris
2. Wine
3. Breast_cancer
4. Digits""")
opt = int(input("Choose dataset: "))
if (opt > 0 and opt <= 4):
    loadData(opt)
else:
    print("Dataset not available")