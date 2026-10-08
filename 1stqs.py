import numpy as np

arr_1d = np.arange(10)
print("1d array : ", arr_1d)

arr_2d = np.random.randint(0,10,size=(3,4))
print("2d array : ", arr_2d)

user_input = input("Enter a numbers seperated by commas : ")
arr = np.array([float(x) for x in user_input.split(",")])
mean = np.mean(arr)
std = np.std(arr)
print(f"The mean of given array is : {mean:.2f}\n")
print(f"The standard deviation of given array is :  {std:.2f}\n")

normalized = (arr - mean) / std
print(f"The normalized array is : \n{normalized}")
