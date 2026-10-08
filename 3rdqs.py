import numpy as np

arr_2d = np.random.randint(1,10,size=(3,3))
print(f"The 2d array : {arr_2d}")
print(f"The third colum is {arr_2d[:,2]}")

user_input = input("Enter numbers seperated by commas : ")
arr_1d = np.array([float(x) for x in user_input.split(",")])
rev = np.flip(arr_1d)
print(f"The reversed array is : {rev}\n")

mat_a = np.random.randint(1,10,size=(2,3))
mat_b = np.random.randint(1,10,size=(3,4))
mat_mul = np.dot(mat_a,mat_b)

user_in = input("enter 9 numbers of the matrix : ")
ar = np.array([float(x) for x in user_in.split(",")])
arrr = ar.reshape(3,3)
print(f"The matrix : {arrr}")
det = np.linalg.det(arrr)
print(f"The determinant of this matrix : {det}")