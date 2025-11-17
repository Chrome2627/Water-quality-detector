import joblib
import numpy as np
from tkinter import *
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound
import os

# Load model files
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")

# Speech function
def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
    except:
        pass  # If speech fails, continue without it

# Validate inputs
def validate_inputs():
    try:
        ph = float(ph_entry.get())
        turbidity = float(turb_entry.get())
        do = float(do_entry.get())
        bod = float(bod_entry.get())
        conductivity = float(cond_entry.get())
        temp = float(temp_entry.get())
        
        # Check limits
        if ph < 0 or ph > 14:
            messagebox.showerror("Error", "pH must be between 0 and 14")
            ph_entry.config(bg="#ffcccc")
            return False
            
        if turbidity < 0 or turbidity > 100:
            messagebox.showerror("Error", "Turbidity must be between 0 and 100 NTU")
            turb_entry.config(bg="#ffcccc")
            return False
            
        if do < 0 or do > 15:
            messagebox.showerror("Error", "Dissolved Oxygen must be between 0 and 15 mg/L")
            do_entry.config(bg="#ffcccc")
            return False
            
        if bod < 0 or bod > 20:
            messagebox.showerror("Error", "BOD must be between 0 and 20 mg/L")
            bod_entry.config(bg="#ffcccc")
            return False
            
        if conductivity < 0 or conductivity > 2000:
            messagebox.showerror("Error", "Conductivity must be between 0 and 2000 µS/cm")
            cond_entry.config(bg="#ffcccc")
            return False
            
        if temp < 0 or temp > 50:
            messagebox.showerror("Error", "Temperature must be between 0 and 50°C")
            temp_entry.config(bg="#ffcccc")
            return False
            
        return True
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers in all fields")
        return False

# Prediction function
def predict():
    # Reset all field colors
    for entry in [ph_entry, turb_entry, do_entry, bod_entry, cond_entry, temp_entry]:
        entry.config(bg="white")
    
    if not validate_inputs():
        return
    
    try:
        vals = [
            float(ph_entry.get()),
            float(turb_entry.get()),
            float(do_entry.get()),
            float(bod_entry.get()),
            float(cond_entry.get()),
            float(temp_entry.get())
        ]

        arr = np.array([vals])
        arr_scaled = scaler.transform(arr)

        pred_class = model.predict(arr_scaled)[0]
        prediction = le.inverse_transform([pred_class])[0]

        if prediction == "Good":
            safety = "SAFE to drink"
            color = "green"
        elif prediction == "Moderate":
            safety = "NOT fully safe (needs treatment)"
            color = "orange"
        else:
            safety = "UNSAFE to drink"
            color = "red"

        final_msg = f"Water Quality: {prediction}\nDrinking Safety: {safety}"
        result_label.config(text=final_msg, fg=color)

        speak(f"Water quality is {prediction}. The water is {safety}.")

    except:
        result_label.config(text="Prediction error", fg="red")

# Clear fields
def clear_fields():
    for entry in [ph_entry, turb_entry, do_entry, bod_entry, cond_entry, temp_entry]:
        entry.delete(0, END)
        entry.config(bg="white")
    result_label.config(text="")

# Create GUI
root = Tk()
root.title("Water Quality Detector ")
root.geometry("500x600")
root.config(bg="#f0faff")

# Header
Label(root, text="Water Quality Detector ", font=("Arial", 20, "bold"), bg="#0275d8", fg="white", pady=10).pack(fill=X)

# Instructions
Label(root, text="Enter realistic water parameters:", font=("Arial", 10), bg="#f0faff").pack(pady=5)

# Main frame
frame = Frame(root, bg="#f0faff")
frame.pack(pady=10)

# Create input fields
def make_row(label, row):
    Label(frame, text=label, font=("Arial", 12), bg="#f0faff").grid(row=row, column=0, padx=10, pady=8, sticky="w")
    entry = Entry(frame, font=("Arial", 12), width=15)
    entry.grid(row=row, column=1, padx=10, pady=8)
    return entry

ph_entry = make_row("pH (0-14):", 0)
turb_entry = make_row("Turbidity (0-100):", 1)
do_entry = make_row("DO (0-15 mg/L):", 2)
bod_entry = make_row("BOD (0-20 mg/L):", 3)
cond_entry = make_row("Conductivity (0-2000):", 4)
temp_entry = make_row("Temperature (0-50°C):", 5)

# Buttons
button_frame = Frame(root, bg="#f0faff")
button_frame.pack(pady=15)

Button(button_frame, text="Predict", font=("Arial", 14), bg="#0275d8", fg="white", width=10, command=predict).grid(row=0, column=0, padx=10)
Button(button_frame, text="Clear", font=("Arial", 14), bg="#6c757d", fg="white", width=10, command=clear_fields).grid(row=0, column=1, padx=10)

# Result label
result_label = Label(root, text="", font=("Arial", 14, "bold"), bg="#f0faff", pady=10)
result_label.pack()

root.mainloop()
