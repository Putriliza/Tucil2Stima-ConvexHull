# CONVEX HULL FOR LINEAR SEPARABILITY TEST VISUALIZATION USING DIVIDE AND CONQUER ALGORITHM

### GENERAL INFORMATION
Divide and conquer algorithm is used to find the convex hull of a set of points on a 2D cartesian plane. This algorithm divide the set of points into several parts based on certain conditions and then do it recursively until all points of the convex hull are found. This program can test the linear separability of 4 dataset from [scikit-learn](https://scikit-learn.org/stable/datasets/toy_dataset.html) (Iris, Wine, Breast_cancer, and Digits).

### REQUIREMENTS
- [python 3](https://www.python.org/downloads/)
- [matplotlib 3.5.1](https://matplotlib.org/stable/users/installing/index.html)
- [numpy 1.22.2](https://numpy.org/install/)
- [pandas 1.4.1](https://pandas.pydata.org/docs/getting_started/install.html)
- [scikit-learn 1.0.2](https://scikit-learn.org/stable/install.html)

### HOW TO RUN
- First, clone this repository
    ```
    https://github.com/Putriliza/Tucil2Stima-ConvexHull.git
    ```
- Open in terminal
- Change directory to src
    ```
    cd src
    ```
- Then run
    ```
    python main.py
    ```

### USAGE
1. Once you run the ```main.py```, the program will show list of datasets than you can test
    ```
    ===================LINEAR SEPARABILITY TEST===================

    1. Iris
    2. Wine
    3. Breast_cancer
    4. Digits       
    Choose dataset:
    ```
2. Input which dataset you want to test (1-4)
3. The program will show list of attributes of the dataset. For example, if you choose 1 (Iris),
    ```
    Available attributes: 
    1. sepal length (cm)  
    2. sepal width (cm)   
    3. petal length (cm)  
    4. petal width (cm)

    Choose attribute (x and y):
    ```
4. Input which attributes you want to test, for example
    ```
    x: 1
    y: 2
    ```
5. The program will ask if you want to save the result. To save the image, type ```'y'```. You can see the image in folder ```\test```
6. The program will show the preview. Close it if you want to continue

### AUTHOR
Putri Nurhaliza - 13520066 <br />
Tugas Kecil 1 IF2211 Algorithm Strategies <br />
Bandung Institute of Technology