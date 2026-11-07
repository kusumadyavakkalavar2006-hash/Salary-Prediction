import pandas as pd
import joblib

# Load the trained model
model = joblib.load("salary_model.pkl")

# Load new test data
given_year = float(input("Enter your experience in years: "))

test_data = pd.DataFrame({"Years": [given_year]})

# Predict salary
predictions = model.predict(test_data)

print(predictions)

# Save predictions
test_data["PredictedSalary"] = predictions
test_data.to_csv("predicted_salaries.csv", index=False)

print("Predictions saved to predicted_salaries.csv")