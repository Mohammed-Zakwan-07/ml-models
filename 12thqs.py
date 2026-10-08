# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
# import matplotlib.pyplot as plt

# df = pd.read_csv("playtennis.csv")
# print("Dataset:\n", df, "\n")
 
# features = ["outlook", "temperature", "humidity", "wind"]
# target = "playtennis"

# encoders = {}
# X = pd.DataFrame()
# for col in features:
#     le = LabelEncoder()
#     X[col] = le.fit_transform(df[col])
#     encoders[col] = le
 
# y_le = LabelEncoder()
# y = y_le.fit_transform(df[target])

# model = DecisionTreeClassifier(criterion="entropy", random_state=0)
# model.fit(X, y)

# print("Decision Tree Rules:\n")
# print(export_text(model, feature_names=features))

# test_data = pd.DataFrame([
#     {"outlook": "sunny", "temperature": "cool", "humidity": "high", "wind": "strong"},
#     {"outlook": "rain", "temperature": "mild", "humidity": "normal", "wind": "weak"},
#     {"outlook": "overcast", "temperature": "hot", "humidity": "normal", "wind": "strong"},
# ])
 
# test_encoded = pd.DataFrame()
# for col in features:
#     test_encoded[col] = encoders[col].transform(test_data[col])
 
# predictions = y_le.inverse_transform(model.predict(test_encoded))
 
# print("Predictions on new examples:")
# for i, row in test_data.iterrows():
#     print(f"{row.to_dict()}  ->  playtennis = {predictions[i]}")

# plot_tree(model, feature_names=features, class_names=y_le.classes_, filled=True)
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

data = pd.read_csv("playtennis.csv")

features = ["outlook", "temperature", "humidity", "wind"]
target = "playtennis"

X = pd.DataFrame()
encoders = {}
for col in features:
  le = LabelEncoder()
  X[col] = le.fit_transform(data[col])
  encoders[col] = le

y_le = LabelEncoder()
y = y_le.fit_transform(data[target])


model = DecisionTreeClassifier(criterion="entropy", random_state=0)
model.fit(X,y)
print(export_text(model, feature_names=features))

test_data =pd.DataFrame([
  {"outlook":"sunny", "temperature":"cold", "humidity":"normal", "wind":"strong"},
  {"outlook":"rain", "temperature":"mild", "humidity":"high", "wind":"strong"},
  {"outlook":"overcast", "temperature":"hot", "humidity":"normal", "wind":"weak"},
])

encoded_test = pd.DataFrame()
for col in features:
  encoded_test[col] = encoders[col].transform(test_data[col])

predictions = y_le.inverse_transform(model.predict(encoded_test))

for i,row in encoded_test.iterrows():
  print(f"{row.to_dict()} -> predictions is {predictions[i]}")

plot_tree(model, feature_names=features, class_names=y_le.classes_, filled=True)
plt.show()
