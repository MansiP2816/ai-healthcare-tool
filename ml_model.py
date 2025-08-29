import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

data = {
    "age": [25, 40, 60, 35],
    "blood_sugar": [85, 150, 200, 120],
    "disease": [0, 1, 1, 0]
}
df = pd.DataFrame(data)

X = df[["age", "blood_sugar"]]
y = df["disease"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "ml_model.pkl")
print("✅ Model saved as ml_model.pkl")
