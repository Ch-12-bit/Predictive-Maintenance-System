# 🔧 Predictive Maintenance System

## 📌 Project Overview

The Predictive Maintenance System is a Machine Learning-based web application that predicts whether a machine is likely to fail based on sensor readings. The project uses a Random Forest Classifier trained on the AI4I 2020 Predictive Maintenance Dataset and provides predictions through an interactive Streamlit dashboard.

---

## 🚀 Features

* Predict machine failure using Machine Learning
* User-friendly Streamlit interface
* Failure probability percentage
* Real-time sensor data visualization
* Interactive bar charts
* Machine health monitoring dashboard
* GitHub-hosted source code

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Joblib

---

## 📊 Input Parameters

The model uses the following machine parameters:

1. Air Temperature (K)
2. Process Temperature (K)
3. Rotational Speed (RPM)
4. Torque (Nm)
5. Tool Wear (minutes)

---

## 🤖 Machine Learning Model

* Algorithm: Random Forest Classifier
* Dataset: AI4I 2020 Predictive Maintenance Dataset
* Objective: Predict machine failure based on operational sensor data

---

## 📂 Project Structure

Predictive_Maintenance/

├── ai4i2020.csv

├── Predictive_Maintenance.ipynb

├── app.py

├── model.pkl

├── requirements.txt

└── README.md

---

## ▶️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Ch-12-bit/Predictive-Maintenance-System.git
```

### 2. Navigate to Project Directory

```bash
cd Predictive-Maintenance-System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Streamlit Application

```bash
python -m streamlit run app.py
```

---

## 📈 Sample Output

The application predicts:

* Machine Operating Normally ✅
* Machine Failure Likely ⚠️

along with the Failure Probability Percentage.

---

## 🎯 Future Enhancements

* Feature importance visualization
* Accuracy dashboard
* Pie chart and gauge chart visualizations
* Cloud deployment using Streamlit Community Cloud
* Real-time IoT sensor integration

---

## 👨‍💻 Author

Chirag Kumar Dubey

B.Tech CSE

KIIT University

GitHub: https://github.com/Ch-12-bit

---

## 📜 License

This project is developed for educational and learning purposes.
