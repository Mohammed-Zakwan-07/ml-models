import numpy as np

mat = np.random.randint(1,10, size=(3,3))
x_axis = np.mean(mat, axis=0)
y_axis = np.mean(mat, axis=1)
print(f"Random matrix : {mat}")
print(f"The mean alog x axis : {x_axis}")
print(f"The mean alog y axis : {y_axis}")

user_input = input("Enter numbers seperated by commas : ")
arr = np.array([float(x) for x in user_input.split(",")])
min = np.min(arr)
max = np.max(arr)
print(f"The minimum value : {min}")
print(f"The maximum value : {max}")

const = int(input("Enter a constant value : "))
ar = arr + const
print(f"The final array after adding {const} is {ar}")

mat_a = np.random.randint(1,10,size=(3,3))
nums = input("Enter 3 numbers seperated by commas : ")
num = np.array([float(x) for x in nums.split(",")]).reshape(3,1)
print("The matrix : ", mat_a)
print(f"the fnal matrix : {mat_a * num}")
