# train_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import joblib

DATA_PATH = "data/water_quality_sample.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

def preprocess(df):
    X = df[['pH','turbidity','do','bod','conductivity','temperature']]
    y = df['label']

    X = X.fillna(X.mean())

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    return X, y_encoded, le

def train_and_save():
    df = load_data()
    X, y, le = preprocess(df)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=le.classes_))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    joblib.dump(clf, "model.pkl")
    joblib.dump(scaler, "scaler.pkl")
    joblib.dump(le, "label_encoder.pkl")

    print("Model, scaler, and label encoder saved.")

if __name__ == "__main__":
    train_and_save()
