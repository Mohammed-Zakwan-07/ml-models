import matplotlib.pyplot as plt

interval = ["10-15", "15-20", "20-25", "25-30", "30-35"]
data = [5,6,9,8,2 ]


plt.figure(figsize=(8,6))
plt.bar(interval, data, color="blue", width=1.0,edgecolor="black")
plt.xlabel("INtervals")
plt.ylabel("Data side")
plt.title("interval vs data")
plt.grid(True)
plt.show()

