# Predictive Maintenance Management System

## Team Members

| Name                 | ID Number   |
| ---------------------| ----------- |
| Sandeep              | 2420030220  |
| Sai Sri Harsha       | 2420030190  |
| Pardha Pranav        | 2420030543  |
| Mohit Nandan Reddy   | 2420030216  |

## Supervisor

**Supervisor Name:** RajKumar Patil

---


## Project Description

The Predictive Maintenance Management System is a software application that uses data analysis and machine learning to predict possible equipment failures before they occur. The system collects historical maintenance records and equipment data such as temperature, vibration, operating hours, pressure, and machine usage. This data is processed and analyzed to identify patterns that indicate potential equipment problems.

The system uses a machine learning model to predict whether equipment is likely to require maintenance. It can classify machines based on their maintenance condition and provide early warnings when a failure is likely to occur. A dashboard can be provided to display equipment status, maintenance history, predicted failures, and important performance indicators.

---

## Objectives

* To predict equipment failures before they occur using machine learning techniques.
* To analyze equipment data such as temperature, vibration, pressure, operating hours, and maintenance history.
* To identify early warning signs of potential machine failures.
* To reduce unexpected equipment breakdowns and minimize machine downtime.
* To reduce maintenance costs by performing maintenance when it is actually required.
* To improve equipment reliability and lifespan through timely maintenance.
* To provide a monitoring dashboard for viewing equipment status, maintenance history, and predicted failure risks.
* To help maintenance teams make data-driven decisions instead of relying only on fixed maintenance schedules.
* To maintain maintenance records and use historical data for future predictions.
* To improve overall operational efficiency by ensuring equipment remains functional and productive.
---

## Key Features

* Equipment Management – Add, update, and monitor information about machines and equipment.
* Real-Time Monitoring – Track equipment parameters such as temperature, vibration, pressure, and operating hours.
* Data Preprocessing – Handle missing values, remove duplicates, clean data, and transform data before analysis.
* Failure Prediction – Use machine learning algorithms to predict whether equipment is likely to fail.
* Maintenance Alerts – Generate alerts when the system detects a high risk of equipment failure.
* Maintenance History – Store and display previous maintenance activities, repairs, and equipment failures.
* Equipment Health Status – Display equipment conditions such as Healthy, Warning, or Critical.
* Interactive Dashboard – Provide graphs, charts, and statistics for easy monitoring and analysis.
* Risk Analysis – Calculate and display the potential failure risk of individual equipment.
* Reports and Analytics – Generate useful reports about equipment performance, failures, and maintenance activities.
* Machine Learning Model – Train and evaluate predictive models using historical equipment data.
* Preventive Action Recommendations – Help maintenance teams decide when equipment should be inspected or serviced.
---

## Technology Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python / Flask
* **AI/NLP:** Python NLP libraries
* **Database:** SQLite
* **Visualization:** Plotly
* **Version Control:** Git and GitHub

---

## Project Structure

```text
Predictive-Maintenance-Management-System/
│
├── README.md
├── Abstract.pdf
├── requirements.txt
├── src/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   └── ...
└── ...
```

> The project structure may be updated as development progresses.

---

## Setup and Execution Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Predictive-Maintenance-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open the Application

Open the URL displayed in the terminal, typically:

```text
http://127.0.0.1:5000
```

---

## Current Phase Status

### Phase 1 – Project Planning

**Status: Completed ✅**

* Project topic finalized
* Problem statement identified
* Project objectives defined
* Initial requirements identified

### Phase 2 – System Design

**Status: In Progress 🔄**

* System architecture planned
* Database structure designed
* User interface planned
* AI/NLP workflow designed

### Phase 3 – Implementation

**Status: Not Started ⏳**

* Frontend development
* Backend development
* Database integration
* NLP/AI analysis implementation

### Phase 4 – Testing and Deployment

**Status: Not Started ⏳**

* System testing
* Bug fixing
* Performance evaluation
* Final deployment

> **Update the status above according to your team's actual current phase.**

---

## Future Enhancements

* Real-Time IoT Integration – Connect IoT sensors to continuously collect temperature, vibration, pressure, and other machine data.
* Advanced Machine Learning Models – Implement algorithms such as Random Forest, XGBoost, LSTM, and other deep learning models to improve prediction accuracy.
* Real-Time Failure Alerts – Send notifications through email, SMS, or mobile applications when a high failure risk is detected.
* Remaining Useful Life (RUL) Prediction – Predict how long equipment can continue operating before maintenance is required.
* Mobile Application – Develop an Android/iOS application so maintenance staff can monitor equipment remotely.
* Automated Maintenance Scheduling – Automatically schedule maintenance based on predicted failure probability and equipment condition.
* Cloud Deployment – Deploy the system on platforms such as AWS, Azure, or Google Cloud for remote access and scalability.
* Advanced Analytics Dashboard – Add interactive dashboards with real-time charts, equipment health scores, failure trends, and maintenance KPIs.

---

## License

This project is developed for academic purposes.

