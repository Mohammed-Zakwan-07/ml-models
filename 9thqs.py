import matplotlib.pyplot  as plt

user_input = input("enter the numbers seperated by comma : ")
data = [float(x) for x in user_input.split(",")]

plt.figure(figsize=(8,6))
plt.boxplot(data)
plt.title("wjat")
plt.grid(True)
plt.show()