import pandas as pd

user_input = input("Enter the numbers seperated by commas : ")
arr = [float(x) for x in user_input.split(",")]
ser = pd.Series(arr)

print("Mean :", ser.mean())
print("Median :", ser.median())
print("Mode :", ser.mode()[0])
print("Variance :", ser.var())
print("Standard deviation :", ser.std())

