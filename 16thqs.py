# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier

# data = load_iris()
# X = data.data 
# y = data.target 
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X_train, y_train)

# accuracy = model.score(X_test, y_test)
# print("Accuracy:", accuracy)

# sample = [[5.1, 3.5, 1.4, 0.2]]
# prediction = model.predict(sample)
# print("Predicted species (0/1/2):", prediction[0])

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data = load_iris()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.8, random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

acc = model.score(X_test, y_test)
print("THe acuurancy is ", acc)

sample = [[5.2,3.5, 1.4,0.2]]
pred = model.predict(sample)[0]
print("The prediction is ", pred)