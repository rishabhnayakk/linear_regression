import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "area": [500, 800, 1000, 1200, 1500],
    "price": [20, 32, 40, 48, 60]
}

df = pd.DataFrame(data)
X = df[["area"]]
y = df["price"]
model = LinearRegression()
model.fit(X, y)
area = float(input("Enter house area in sq ft: "))
prediction = model.predict([[area]])
print(f"Predicted price: ₹{prediction[0]:.2f} lakh")