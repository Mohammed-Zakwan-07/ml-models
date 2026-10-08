import matplotlib.pyplot  as plt

time = [0,1,2,3,4,5,6]
speed = [0,3,7,12,20,30,45.6]

plt.plot(time,speed,marker="o")
plt.xlabel("TIme")
plt.ylabel("speed")
plt.title("Speed over time")
plt.grid(True)
plt.show()

plt.bar(time,speed,color="red", edgecolor="black")
plt.xlabel("TIme")
plt.ylabel("speed")
plt.title("Speed over time")
plt.grid(True)
plt.show()