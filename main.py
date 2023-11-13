import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # Convert height to meters
        bmi = weight / (height ** 2)
        bmi_value.set(f"{bmi:.2f}")

        if bmi < 18.5:
            bmi_category.set("Underweight")
        elif 18.5 <= bmi < 24.9:
            bmi_category.set("Normal weight")
        elif 24.9 <= bmi < 29.9:
            bmi_category.set("Overweight")
        else:
            bmi_category.set("Obese")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for weight and height.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Define StringVars to hold the BMI value and category
bmi_value = tk.StringVar()
bmi_category = tk.StringVar()

# Create and place widgets
tk.Label(root, text="Enter your weight (in kg):").grid(row=0, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1)

tk.Label(root, text="Enter your height (in cm):").grid(row=1, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1)

button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.grid(row=2, column=0, columnspan=2)

tk.Label(root, text="Your BMI is:").grid(row=3, column=0)
label_bmi_value = tk.Label(root, textvariable=bmi_value)
label_bmi_value.grid(row=3, column=1)

tk.Label(root, text="You are classified as:").grid(row=4, column=0)
label_bmi_category = tk.Label(root, textvariable=bmi_category)
label_bmi_category.grid(row=4, column=1)

# Start the event loop
root.mainloop()


