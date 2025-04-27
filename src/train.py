import os
import mlflow
import mlflow.keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Load Dataset
df = pd.read_csv('material_desc.csv')  # <-- Make sure file is in correct path
df = df.dropna()

# Define Features and Target
X = df[['Hardness', 'Toughness', 'Density (g/cm³)', 'Yield Stress (MPa)']]
y = df['Application']

# Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

le = LabelEncoder()
y_encoded = le.fit_transform(y)
num_classes = len(np.unique(y_encoded))
y_one_hot = to_categorical(y_encoded, num_classes=num_classes)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_one_hot, test_size=0.2, random_state=42)

# Model Definition
model = Sequential([
    Dense(12, activation='relu', input_dim=4),
    Dense(8, activation='relu'),
    Dense(num_classes, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Set MLflow tracking
mlflow.set_tracking_uri("file:///tmp/mlruns")
mlflow.set_experiment("Material_Application_Classifier")

with mlflow.start_run():
    # Train the Model
    history = model.fit(X_train, y_train, epochs=200, batch_size=5, validation_data=(X_test, y_test))

    # Evaluate the Model
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"✅ Test Accuracy: {accuracy:.4f}")

    # Log Metrics
    mlflow.log_metric("test_loss", loss)
    mlflow.log_metric("test_accuracy", accuracy)

    # Log the Model
    mlflow.keras.log_model(model, "model")

    print(f"✅ Model saved in run {mlflow.active_run().info.run_id}")
