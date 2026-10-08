# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
 
# data = pd.read_csv("clients_data.csv")
 
# x = data[["Exercise_Time_Hours"]]
# y = data["Calories_Burned"]
 
# model = LinearRegression()
# model.fit(x, y)
 
# m = model.coef_[0]
# c = model.intercept_
 
# print(f"Slope (m) : {m}")
# print(f"Intercept (c) : {c}")
# print(f"Regression equation: y = {m}x + {c}")

# predict_x = 6
# predict_y = model.predict([[predict_x]])[0]
# print(f"Predicted calories burnt for {predict_x} hours: {predict_y}")

# plt.scatter(x, y, color="blue", label="Data points")
# plt.plot(x, model.predict(x), color="red", label=f"y = {m:.2f}x + {c:.2f}")
# plt.scatter(predict_x, predict_y, color="green", marker="D", label=f"Prediction ({predict_x} hrs)")
# plt.title("Exercise Time vs Calories Burnt")
# plt.xlabel("Exercise Time (hours)")
# plt.ylabel("Calories Burnt")
# plt.legend()
# plt.grid(True)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.DataFrame([
  {"time" : 1, "calories_burned" : 200},
  {"time" : 2, "calories_burned" : 400},
  {"time" : 3, "calories_burned" : 600},
  {"time" : 4, "calories_burned" : 800},
  {"time" : 5, "calories_burned" : 1000},
])

X = df[["time"]]
y = df[["calories_burned"]]

model = LinearRegression()
model.fit(X,y)

m = model.coef_[0]
c = model.intercept_

print("The slope m:", model.coef_[0])
print("The intercept c: ", model.intercept_)
print(f"The linear regression line y = {m}x + {c}")

pred_x = 6
pred = model.predict([[pred_x]])[0]
print(f"The predicted value for the {pred_x} is {pred}")

y_pred = model.predict(X)
plt.figure(figsize=(8,6))
plt.plot(X,y,c="red", label="Actual data")
plt.scatter(X,y_pred, c="blue", marker="x", label="Predicted")
plt.xlabel("The x axis")
plt.ylabel("The y axis")
plt.title("The the linear regression model")
plt.legend()
plt.show()


