import numpy as np

evenly_spaced = np.linspace(0,1,10)
print(f"Evenly spaced values between 0 and 1 : {evenly_spaced}")

mat = np.eye(3)
print(f"3x3 identity matrix : \n {mat}")

user_input = input("Enter 10 numbers seperated by commas : ")
arr = np.array([float(x) for x in user_input.split(",")])
reshaped_array  = arr.reshape(2,5)
print(f"The original arr : {arr}\n")
print(f"After reshaping : \n {reshaped_array}")

ver_arr = np.vstack((arr, evenly_spaced))
hor_arr = np.hstack((arr, evenly_spaced))
print(f"Vertical stack of two arrays : \n{ver_arr}")
print(f"horizpntal stack of two arrays : \n{hor_arr}")

