import pandas as pd
import matplotlib.pyplot as plt


catogries = []
values = []

n = int(input("how many values : "))

for i in range(n):
  cat = input("Enter the category : ")
  catogries.append(cat)
  value = input("Enter the value for it : ")
  values.append(value)


plt.bar(catogries, values, color="red")
plt.show()