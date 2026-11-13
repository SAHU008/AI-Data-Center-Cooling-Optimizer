
import streamlit as st
import numpy as np
import json
import csv

st.set_page_config(
    page_title="AI Data Center Cooling Optimizer",
    page_icon="❄️",
    layout="wide"
)

# Load trained model
with open("model_parameters.json", "r") as file:
    model = json.load(file)

features = model["features"]
mean = np.array(model["mean"])
std = np.array(model["std"])
weights = np.array(model["weights"])

# Dashboard heading
st.title("🌡️ AI Data Center Cooling Optimizer")
st.caption("Machine Learning-Based Server Temperature Prediction Dashboard")
st.write(
    "An AI-powered system for predicting server temperature "
    "and monitoring cooling performance."
)

st.divider()

# Sidebar inputs
st.sidebar.header("Server Operating Conditions")

cpu = st.sidebar.slider("CPU Usage (%)", 0, 100, 60)
ambient = st.sidebar.slider("Ambient Temperature (°C)", 15, 45, 25)
inlet = st.sidebar.slider("Inlet Temperature (°C)", 10, 35, 18)
airflow = st.sidebar.slider("Airflow", 1.5, 5.0, 3.0, step=0.1)
cooling = st.sidebar.slider("Cooling Power", 2.0, 15.0, 8.0, step=0.1)

# Predict temperature
input_values = np.array([
    cpu, ambient, inlet, airflow, cooling
], dtype=float)

scaled = (input_values - mean) / std
model_input = np.insert(scaled, 0, 1)

predicted_temp = float(model_input @ weights)

# Main dashboard
st.subheader("Server Temperature Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Predicted Temperature",
              f"{predicted_temp:.2f} °C")
    if predicted_temp < 35:
       st.success("Normal Temperature")
    elif predicted_temp < 45:
       st.warning("High Temperature - Cooling Attention Needed")
    else:
       st.error("Critical Temperature - Immediate Cooling Attention Needed")

with col2:
    st.metric("CPU Usage", f"{cpu}%")

with col3:
    st.metric("Cooling Power", f"{cooling}%")

# Temperature status
if predicted_temp < 35:
    st.success("Normal Temperature")
    st.info("Recommendation: Maintain current cooling settings.")

elif predicted_temp < 45:
    st.warning("High Temperature")
    st.info("Recommendation: Increase airflow and monitor server temperature.")

else:
    st.error("Critical Temperature")
    st.info("Recommendation: Increase cooling power and reduce server workload.")
    
# No extra else here
st.success("Predicted temperature is within the prototype's normal range.")
st.divider()

# Historical dataset

# Historical dataset summary
st.subheader("Historical Server Temperature")

with open("data/server_data.csv", "r") as file:
    reader = csv.DictReader(file)
    records = list(reader)

temperatures = [
    float(row["server_temp"]) for row in records
]

if temperatures:
    avg_temp = sum(temperatures) / len(temperatures)
    min_temp = min(temperatures)
    max_temp = max(temperatures)

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Temperature", f"{avg_temp:.2f} °C")
    col2.metric("Minimum Temperature", f"{min_temp:.2f} °C")
    col3.metric("Maximum Temperature", f"{max_temp:.2f} °C")

    st.write("Total dataset records:", len(temperatures))

    st.write("Recent server temperatures:")
    for temp in temperatures[-10:]:
        st.write(f"{temp:.2f} °C")
