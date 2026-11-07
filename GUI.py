import tkinter as tk
from tkinter import messagebox
import joblib
import pandas as pd
import os

# -----------------------------
# Load trained model
# -----------------------------
MODEL_FILE = "salary_model.pkl"

if not os.path.exists(MODEL_FILE):
    messagebox.showerror(
        "Model Not Found",
        "salary_model.pkl not found!\n\nPlease run training.py first."
    )
    raise SystemExit

model = joblib.load(MODEL_FILE)


# -----------------------------
# Prediction Function
# -----------------------------
def predict_salary():

    try:
        years = float(year_entry.get())

        if years < 0:
            messagebox.showwarning(
                "Invalid Input",
                "Years of experience cannot be negative."
            )
            return

        # Create test data
        test_data = pd.DataFrame({
            "Years": [years]
        })

        # Predict salary
        prediction = model.predict(test_data)[0]

        # Display result
        result_label.config(
            text=f"₹ {prediction:,.2f}"
        )

        # Save prediction
        result_data = pd.DataFrame({
            "Years": [years],
            "PredictedSalary": [prediction]
        })

        result_data.to_csv(
            "predicted_salaries.csv",
            mode="a",
            header=not os.path.exists("predicted_salaries.csv"),
            index=False
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number.\nExample: 5"
        )


# -----------------------------
# Clear Function
# -----------------------------
def clear_data():

    year_entry.delete(0, tk.END)
    result_label.config(
        text="₹ 0.00"
    )


# -----------------------------
# Exit Function
# -----------------------------
def exit_app():
    root.destroy()


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("Salary Prediction System")
root.geometry("650x550")
root.resizable(False, False)

# Background
root.configure(bg="#EAF4FF")


# -----------------------------
# Header
# -----------------------------
header = tk.Frame(
    root,
    bg="#4B0082",
    height=110
)

header.pack(fill="x")

title_label = tk.Label(
    header,
    text="SALARY PREDICTION",
    font=("Arial", 28, "bold"),
    fg="white",
    bg="#4B0082"
)

title_label.pack(pady=(20, 5))

subtitle_label = tk.Label(
    header,
    text="Machine Learning • Linear Regression",
    font=("Arial", 12),
    fg="#E8D9FF",
    bg="#4B0082"
)

subtitle_label.pack()


# -----------------------------
# Main Card
# -----------------------------
card = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="groove"
)

card.place(
    x=75,
    y=145,
    width=500,
    height=330
)


# Information
info_label = tk.Label(
    card,
    text="Predict your salary based on experience",
    font=("Arial", 16, "bold"),
    fg="#4B0082",
    bg="white"
)

info_label.pack(pady=(25, 20))


# Years Label
year_label = tk.Label(
    card,
    text="Years of Experience",
    font=("Arial", 13, "bold"),
    fg="#333333",
    bg="white"
)

year_label.pack()


# Entry
year_entry = tk.Entry(
    card,
    font=("Arial", 18),
    justify="center",
    width=20,
    bd=2,
    relief="solid"
)

year_entry.pack(pady=10)

year_entry.focus()


# -----------------------------
# Predict Button
# -----------------------------
predict_button = tk.Button(
    card,
    text="🔮  PREDICT SALARY",
    command=predict_salary,
    font=("Arial", 13, "bold"),
    bg="#6A0DAD",
    fg="white",
    activebackground="#8A2BE2",
    activeforeground="white",
    width=22,
    height=2,
    bd=0,
    cursor="hand2"
)

predict_button.pack(pady=10)


# -----------------------------
# Result
# -----------------------------
result_title = tk.Label(
    card,
    text="Predicted Salary",
    font=("Arial", 12, "bold"),
    fg="#555555",
    bg="white"
)

result_title.pack(pady=(5, 0))


result_label = tk.Label(
    card,
    text="₹ 0.00",
    font=("Arial", 25, "bold"),
    fg="#008000",
    bg="white"
)

result_label.pack()


# -----------------------------
# Bottom Buttons
# -----------------------------
button_frame = tk.Frame(
    root,
    bg="#EAF4FF"
)

button_frame.pack(
    side="bottom",
    pady=20
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    command=clear_data,
    font=("Arial", 11, "bold"),
    bg="#FFB703",
    fg="black",
    width=12,
    height=2,
    bd=0,
    cursor="hand2"
)

clear_button.grid(
    row=0,
    column=0,
    padx=10
)


exit_button = tk.Button(
    button_frame,
    text="EXIT",
    command=exit_app,
    font=("Arial", 11, "bold"),
    bg="#E63946",
    fg="white",
    width=12,
    height=2,
    bd=0,
    cursor="hand2"
)

exit_button.grid(
    row=0,
    column=1,
    padx=10
)


# -----------------------------
# Footer
# -----------------------------
footer = tk.Label(
    root,
    text="Salary Prediction using Machine Learning",
    font=("Arial", 9),
    fg="#666666",
    bg="#EAF4FF"
)

footer.place(
    x=190,
    y=520
)


# -----------------------------
# Run Application
# -----------------------------
root.mainloop()