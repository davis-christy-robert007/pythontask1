import numpy as np
"""
arr= np.array([1,2,3,4,5,6])
print(arr)
mat=np.array([[1,2,3],[4,5,6]])
print(mat)
"""
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Traversing a 2d array row by row :")
for row in arr:
    for element in row :
        print(element,end=" ")
    print()