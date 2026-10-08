import pandas as pd

names = []
ages = []
citys = []

n = int(input("Enter the number a rows in the dataframe : "))

for i in range(n):
  name = input("Enter the name of the student : ")
  names.append(name)
  age = int(input("Enter the age of the student : "))
  ages.append(age)
  city = input("Enter the city of the student : ")
  citys.append(city)

df = pd.DataFrame({"Name":names, "Age":ages, "Citys":citys})

print(df)
print(df.dtypes)
