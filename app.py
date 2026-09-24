from flask import Flask, render_template, request, jsonify
import sqlite3
import os
import joblib
import pandas as pd
from datetime import datetime

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "maintenance.db")
MODEL_PATH = os.path.join(BASE_DIR, "model", "maintenance_model.joblib")

FEATURES = [
    "temperature",
    "vibration",
    "pressure",
    "runtime_hours",
    "machine_age",
    "load_percentage"
]

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            machine_type TEXT NOT NULL,
            location TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Operational',
            created_at TEXT NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS maintenance_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_id INTEGER,
            prediction TEXT NOT NULL,
            probability REAL NOT NULL,
            temperature REAL NOT NULL,
            vibration REAL NOT NULL,
            pressure REAL NOT NULL,
            runtime_hours REAL NOT NULL,
            machine_age REAL NOT NULL,
            load_percentage REAL NOT NULL,
            recommendation TEXT NOT NULL,
            created_at TEXT NOT NULL,
            FOREIGN KEY(machine_id) REFERENCES machines(id)
        )
    """)

    count = conn.execute("SELECT COUNT(*) FROM machines").fetchone()[0]
    if count == 0:
        sample_machines = [
            ("CNC Machine 01", "CNC", "Production Floor A", "Operational"),
            ("Hydraulic Press 02", "Hydraulic Press", "Production Floor B", "Operational"),
            ("Compressor 03", "Compressor", "Utility Room", "Maintenance Due"),
            ("Lathe Machine 04", "Lathe", "Production Floor A", "Operational"),
            ("Pump 05", "Pump", "Utility Room", "Warning")
        ]
        for name, mtype, location, status in sample_machines:
            conn.execute(
                "INSERT INTO machines (name, machine_type, location, status, created_at) VALUES (?, ?, ?, ?, ?)",
                (name, mtype, location, status, datetime.now().isoformat(timespec="seconds"))
            )
    conn.commit()
    conn.close()

def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)

def recommendation(risk, probability):
    if risk == "High":
        return "Schedule maintenance immediately and inspect critical components."
    if risk == "Medium":
        return "Schedule preventive maintenance soon and monitor sensor values."
    return "Machine is operating normally. Continue routine monitoring."

@app.route("/")
def dashboard():
    conn = get_db()
    machines = conn.execute("SELECT * FROM machines ORDER BY id DESC").fetchall()
    logs = conn.execute("""
        SELECT maintenance_logs.*, machines.name AS machine_name
        FROM maintenance_logs
        LEFT JOIN machines ON machines.id = maintenance_logs.machine_id
        ORDER BY maintenance_logs.id DESC LIMIT 8
    """).fetchall()

    total = conn.execute("SELECT COUNT(*) FROM machines").fetchone()[0]
    high = conn.execute("SELECT COUNT(*) FROM maintenance_logs WHERE prediction='High'").fetchone()[0]
    medium = conn.execute("SELECT COUNT(*) FROM maintenance_logs WHERE prediction='Medium'").fetchone()[0]
    low = conn.execute("SELECT COUNT(*) FROM maintenance_logs WHERE prediction='Low'").fetchone()[0]
    conn.close()

    return render_template(
        "dashboard.html",
        machines=machines,
        logs=logs,
        total=total,
        high=high,
        medium=medium,
        low=low
    )

@app.route("/predict", methods=["POST"])
def predict():
    model = load_model()
    if model is None:
        return jsonify({"error": "Model not found. Run train_model.py first."}), 500

    try:
        payload = request.get_json(force=True)
        values = {f: float(payload[f]) for f in FEATURES}
        df = pd.DataFrame([values], columns=FEATURES)

        prediction = model.predict(df)[0]
        probabilities = model.predict_proba(df)[0]
        classes = list(model.classes_)
        probability = float(probabilities[classes.index(prediction)])

        rec = recommendation(prediction, probability)

        machine_id = payload.get("machine_id")
        conn = get_db()
        conn.execute("""
            INSERT INTO maintenance_logs
            (machine_id, prediction, probability, temperature, vibration, pressure,
             runtime_hours, machine_age, load_percentage, recommendation, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            machine_id if machine_id else None,
            prediction,
            probability,
            values["temperature"],
            values["vibration"],
            values["pressure"],
            values["runtime_hours"],
            values["machine_age"],
            values["load_percentage"],
            rec,
            datetime.now().isoformat(timespec="seconds")
        ))

        if machine_id:
            new_status = "Warning" if prediction == "Medium" else (
                "Maintenance Due" if prediction == "High" else "Operational"
            )
            conn.execute("UPDATE machines SET status=? WHERE id=?", (new_status, machine_id))

        conn.commit()
        conn.close()

        return jsonify({
            "prediction": prediction,
            "probability": round(probability * 100, 2),
            "recommendation": rec
        })

    except (KeyError, TypeError, ValueError) as exc:
        return jsonify({"error": f"Invalid input: {exc}"}), 400

@app.route("/machines")
def machines():
    conn = get_db()
    rows = conn.execute("SELECT * FROM machines ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("machines.html", machines=rows)

@app.route("/maintenance")
def maintenance():
    conn = get_db()
    logs = conn.execute("""
        SELECT maintenance_logs.*, machines.name AS machine_name
        FROM maintenance_logs
        LEFT JOIN machines ON machines.id = maintenance_logs.machine_id
        ORDER BY maintenance_logs.id DESC
    """).fetchall()
    conn.close()
    return render_template("maintenance.html", logs=logs)

@app.route("/api/stats")
def stats():
    conn = get_db()
    data = {
        "labels": ["High", "Medium", "Low"],
        "values": [
            conn.execute("SELECT COUNT(*) FROM maintenance_logs WHERE prediction='High'").fetchone()[0],
            conn.execute("SELECT COUNT(*) FROM maintenance_logs WHERE prediction='Medium'").fetchone()[0],
            conn.execute("SELECT COUNT(*) FROM maintenance_logs WHERE prediction='Low'").fetchone()[0]
        ]
    }
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
