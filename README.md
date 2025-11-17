#  Water Quality Detector

A machine learning-based Python application that predicts water quality and provides drinking safety recommendations using measurable parameters.

##  Project Overview

This project classifies water samples into three categories (**Good**, **Moderate**, **Poor**) using a Random Forest machine learning model. It features multiple interfaces including a professional GUI and text-to-speech output for enhanced accessibility.

## Features

-  **Real-time Water Quality Prediction**
-  **Professional GUI with Input Validation**
-  **Voice Output for Accessibility** 
-  **Drinking Safety Recommendations**
-  **Input Range Validation** (Realistic Limits)
-  **Color-coded Results** (Green/Orange/Red)
-  **Multiple Interface Options** (CLI & GUI)

##  Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone/Download the Project
```bash
# Create project folder
mkdir water_quality_detector
cd water_quality_detector
```

### Step 2: Install Dependencies
```bash
pip install numpy pandas scikit-learn joblib gtts playsound
```

##  Project Structure
```
water_quality_detector/
│
├── data/
│   └── water_quality_sample.csv          # Dataset
│
├── train_model.py                        # Model training script
├── app.py                               # Main GUI application
├── requirements.txt                     # Dependencies list
│
├── model.pkl                           # Trained ML model (auto-generated)
├── scaler.pkl                          # Data scaler (auto-generated)
└── label_encoder.pkl                   # Label encoder (auto-generated)
```
#### REMEMBER PUT THE water_quality_sample.cvs in a new folder name data like shown in above ####

##  Usage

### Step 1: Train the Model (Run Once)
```bash
python train_model.py
```
This will:
- Train the Random Forest model
- Evaluate performance
- Save model files (`model.pkl`, `scaler.pkl`, `label_encoder.pkl`)

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Using the Application
1. Enter water parameters in the GUI:
   - **pH** (0-14)
   - **Turbidity** (0-100 NTU)
   - **Dissolved Oxygen** (0-15 mg/L)
   - **BOD** (0-20 mg/L)
   - **Conductivity** (0-2000 µS/cm)
   - **Temperature** (0-50°C)

2. Click **"Predict Water Quality"**
3. View results with color-coded safety recommendations
4. Listen to voice feedback

##  Sample Test Values

| Quality | Sample Input | Expected Output |
|---------|--------------|-----------------|
| **Good** | `7.2, 1.3, 7.8, 1.4, 140, 26` | Safe to drink ✅ |
| **Moderate** | `7.8, 5.0, 6.0, 3.5, 400, 28` | Not fully safe ⚠️ |
| **Poor** | `5.0, 8.5, 2.0, 6.0, 800, 32` | Unsafe to drink ❌ |

##  Technical Details

### Machine Learning Model
- **Algorithm**: Random Forest Classifier
- **Accuracy**: 92-100% (on demo dataset)
- **Features**: 6 water quality parameters
- **Classes**: Good (0), Moderate (1), Poor (2)

### Libraries Used
- `scikit-learn` - Machine learning
- `pandas`, `numpy` - Data processing
- `tkinter` - GUI development
- `gTTS`, `playsound` - Text-to-speech
- `joblib` - Model persistence

##  Model Performance

```
Classification Report:
              precision    recall  f1-score   support

        Good       1.00      1.00      1.00         2
    Moderate       1.00      1.00      1.00         2
        Poor       1.00      1.00      1.00         2

    accuracy                           1.00         6
```

##  Project Information

**Developed By:**
- Rudraksh Bargali (S24CSEU0380)
- Vedansh Sharma (S24CSEU2381)

**Academic Program:** BTech in Computer Science  
**Supervisor:** Lab Faculty Name  
**Institution:** School of Computer Science Engineering and Technology

##  Future Enhancements

- [ ] Web deployment (Flask/Streamlit)
- [ ] Mobile application
- [ ] Hardware integration (Arduino sensors)
- [ ] Real-time sensor data processing
- [ ] Geographic mapping of results
- [ ] Larger real-world dataset integration

##  Troubleshooting

### Common Issues:

1. **ModuleNotFoundError**
   ```bash
   # Install missing packages
   python -m pip install [package-name]
   ```

2. **FileNotFoundError: model.pkl**
   - Run `train_model.py` first before `app.py`

3. **Speech not working**
   - Ensure internet connection for gTTS
   - Check audio output device

### Input Validation:
The application includes strict input validation:
- pH: 0-14
- Turbidity: 0-100 NTU
- DO: 0-15 mg/L
- BOD: 0-20 mg/L
- Conductivity: 0-2000 µS/cm
- Temperature: 0-50°C

##  Support

For questions or issues regarding this project, please contact the development team.


** If you find this project useful, please give it a star!**

*Last Updated: November 2025*
