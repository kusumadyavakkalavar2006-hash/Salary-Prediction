import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("data.csv")

# Split features and target
X = data[["Years"]]
y = data["Salary"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
joblib.dump(model, "salary_model.pkl")

print("Model trained and saved as salary_model.pkl")