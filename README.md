# 🌡️ AI Data Center Cooling Optimizer

An AI-powered project that predicts server temperatures and provides cooling recommendations using Machine Learning.

## 🚀 Project Overview

The AI Data Center Cooling Optimizer is designed to demonstrate how machine learning can help monitor server temperatures and support cooling decisions in data centers.

The system predicts server temperature based on:
- CPU Usage
- Ambient Temperature
- Inlet Temperature
- Airflow
- Cooling Power

It also displays temperature status and suggests cooling actions.

## ✨ Features

- Server temperature prediction
- Interactive Streamlit dashboard
- Normal, Warning and Critical temperature indicators
- Automatic cooling recommendations
- Model performance evaluation
- Simulated dataset containing 2,000 records

## 🛠️ Technologies Used

- Python
- NumPy
- Machine Learning (Linear Regression)
- Streamlit
- CSV Dataset

## 📊 Model Performance

| Metric | Result |
|---|---:|
| MAE | 0.8137°C |
| RMSE | 0.9994°C |
| R² Score | 0.9864 |

*These results are from testing on the simulated dataset.*

## 📁 Project Structure

```text
AI_Data_Center_Cooling/
│
├── app.py
├── train_model.py
├── model_parameters.json
├── requirements.txt
├── .gitignore
│
└── data/
    ├── generate_data.py
    └── server_data.csv
```

## ⚙️ Installation and Setup

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder:

```bash
cd AI-Data-Center-Cooling-Optimizer
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the dashboard:

```bash
streamlit run app.py
```

## 🎯 Project Objective

To explore how machine learning can support data center temperature monitoring and cooling management.

## ⚠️ Disclaimer

This project uses simulated data for educational and demonstration purposes. It is not connected to real data center sensors and should not be used for actual cooling control.

## 👩‍💻 Author

Developed as an AI/ML learning and portfolio project.

## ⭐ Support

If you find this project interesting, consider giving the repository a star!
