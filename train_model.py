import os
import random
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = os.path.join(BASE_DIR, "model")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

random.seed(42)

rows = []
for _ in range(1500):
    temperature = round(random.uniform(45, 110), 2)
    vibration = round(random.uniform(0.5, 9.0), 2)
    pressure = round(random.uniform(1.0, 8.0), 2)
    runtime_hours = round(random.uniform(100, 15000), 2)
    machine_age = round(random.uniform(0.5, 15), 2)
    load_percentage = round(random.uniform(20, 100), 2)

    score = 0
    if temperature > 90: score += 2
    elif temperature > 78: score += 1

    if vibration > 6.5: score += 2
    elif vibration > 4.5: score += 1

    if pressure > 6.5 or pressure < 1.8: score += 2
    elif pressure > 5.5 or pressure < 2.3: score += 1

    if runtime_hours > 11000: score += 2
    elif runtime_hours > 7500: score += 1

    if machine_age > 10: score += 2
    elif machine_age > 6: score += 1

    if load_percentage > 88: score += 2
    elif load_percentage > 72: score += 1

    # Small noise makes the dataset less perfectly rule-based.
    score += random.choice([-1, 0, 0, 0, 1])

    if score >= 7:
        risk = "High"
    elif score >= 4:
        risk = "Medium"
    else:
        risk = "Low"

    rows.append([
        temperature, vibration, pressure, runtime_hours,
        machine_age, load_percentage, risk
    ])

columns = [
    "temperature", "vibration", "pressure", "runtime_hours",
    "machine_age", "load_percentage", "risk"
]

df = pd.DataFrame(rows, columns=columns)
csv_path = os.path.join(DATA_DIR, "machine_sensor_data.csv")
df.to_csv(csv_path, index=False)

X = df.drop(columns=["risk"])
y = df["risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    max_depth=8
)
model.fit(X_train, y_train)

pred = model.predict(X_test)
accuracy = accuracy_score(y_test, pred)

model_path = os.path.join(MODEL_DIR, "maintenance_model.joblib")
joblib.dump(model, model_path)

print(f"Model accuracy: {accuracy:.2%}")
print(classification_report(y_test, pred))
print(f"Dataset saved to: {csv_path}")
print(f"Model saved to: {model_path}")
