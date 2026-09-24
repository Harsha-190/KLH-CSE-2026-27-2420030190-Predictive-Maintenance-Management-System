# Predictive Maintenance Management System

A student-friendly web application that predicts machine maintenance risk using sensor and operational data.

## Technology Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- Scikit-learn
- Pandas
- SQLite
- Random Forest Machine Learning

## Main Features

1. Interactive dashboard
2. Machine inventory
3. Maintenance-risk prediction
4. High / Medium / Low risk classification
5. Prediction probability
6. Automatic maintenance recommendation
7. SQLite prediction history
8. Machine status updates
9. Maintenance history page
10. Chart showing prediction distribution

## Input Features

- Temperature (°C)
- Vibration (mm/s)
- Pressure (bar)
- Runtime Hours
- Machine Age (years)
- Load Percentage (%)

## Project Structure

```text
predictive_maintenance_management_system/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── maintenance.db
│
├── data/
│   └── machine_sensor_data.csv
│
├── model/
│   └── maintenance_model.joblib
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── machines.html
│   └── maintenance.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

## How to Run

### 1. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python train_model.py
```

This creates the dataset and Random Forest model.

### 4. Start Flask

```bash
python app.py
```

### 5. Open the application

Open:

```text
http://127.0.0.1:5000
```

## How the Prediction Works

The Random Forest model learns relationships between machine sensor values and maintenance risk.

- Low = normal operating condition
- Medium = possible maintenance requirement
- High = immediate maintenance attention recommended

The dataset included in this student project is synthetic. For a real deployment, replace it with actual IoT/industrial sensor data and verified maintenance records.

## Future Enhancements

- IoT sensor integration
- Real-time alerts
- Email/SMS notifications
- Remaining Useful Life prediction
- User authentication
- Advanced analytics
- Cloud deployment
- Multiple ML models
- PDF maintenance reports
