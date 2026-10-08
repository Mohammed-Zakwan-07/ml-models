# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.naive_bayes import CategoricalNB

# df = pd.read_csv("fauna_dataset.csv")

# features = ["Swim", "Fly", "Crawl"]
# target = ["Class"]

# encoders = {}

# X = pd.DataFrame()

# for col in features:
#     le = LabelEncoder()
#     X[col] = le.fit_transform(df[col])
#     encoders[col] = le

# y_le = LabelEncoder()
# y = y_le.fit_transform(df[target[0]])

# model = CategoricalNB(alpha=1.0)
# model.fit(X, y)
# print("The model is trained successfully")

# test_data = pd.DataFrame([
#     {"Swim": "Slow", "Fly": "Rarely", "Crawl": "No"}
# ])

# encoded = pd.DataFrame()

# for col in features:
#     encoded[col] = encoders[col].transform(test_data[col])

# predictions = y_le.inverse_transform(model.predict(encoded))

# probabilities = model.predict_proba(encoded)[0]

# print("\nTest Data:")
# print(test_data)

# print("\nProbabilities:")

# for cls, prob in zip(y_le.classes_, probabilities):
#     print(f"P({cls} | X) = {prob:.4f}")

# print(f"\nPredicted class label: {predictions[0]}")

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB

data = pd.read_csv("fauna_dataset.csv")

features = ["swim", "fly", "crawl"]
target = ["class"]

encoders = {}
X = pd.DataFrame()
for col in features:
  le = LabelEncoder()
  X[col] = le.fit_transform(data[col])
  encoders[col] = le

y_le = LabelEncoder()
y = y_le.fit_transform(data[target])

model = CategoricalNB(alpha=1.0)
model.fit(X,y)

test_data = pd.DataFrame([
  {"swim":"Slow", "fly":"Rarely" ,"crawl":"Yes"},
  {"swim":"Fast", "fly":"Never" ,"crawl":"Yes"},
  {"swim":"Slow", "fly":"Often" ,"crawl":"No"},
])

encoded_test = pd.DataFrame()
for col in features:
  encoded_test[col] = encoders[col].transform(test_data[col])

predictions = y_le.inverse_transform(model.predict(encoded_test))
probabilities = model.predict_proba(encoded_test)

print("The test data")
print(test_data)

for cls, prob in zip(y_le.classes_, probabilities):
  print(f"P({cls} | X) = {prob}")

print("the predictions : ", predictions[0])