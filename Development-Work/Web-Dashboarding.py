# Interactive web applications

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os
from io import BytesIO

st.set_page_config(page_title="Security Pipeline Dashboard", layout="wide")
st.title("🛡️ AI-Driven Security Pipeline Dashboard")

# Load CSV logs with fallback
@st.cache_data
def load_log(file_path):
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            if df.empty:
                st.warning(f"⚠️ {file_path} is empty.")
            return df
        except pd.errors.EmptyDataError:
            st.error(f"❌ Error reading {file_path} (empty or invalid format).")
            return pd.DataFrame()
    else:
        st.warning(f"⚠️ File not found: {file_path}")
        return pd.DataFrame()

monitor_df = load_log("monitoring_log.csv")
detect_df = load_log("detection_log.csv")
quarantine_df = load_log("quarantine_log.csv")
resolution_df = load_log("resolution_log.csv")

# Export utility
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# --- MONITORING PHASE ---
st.header("🔍 Monitoring Phase")
if not monitor_df.empty:
    st.dataframe(monitor_df.head(10))
    st.bar_chart(monitor_df['anomaly'].value_counts())
    if 'modification_time' in monitor_df.columns:
        fig, ax = plt.subplots()
        monitor_df['modification_time'] = pd.to_datetime(monitor_df['modification_time'], unit='s')
        monitor_df.groupby(monitor_df['modification_time'].dt.date)['anomaly'].value_counts().unstack().fillna(0).plot(ax=ax)
        ax.set_title("📆 Anomaly Trends Over Time")
        ax.set_ylabel("File Count")
        st.pyplot(fig)
    st.download_button("📥 Download Monitoring Data", convert_df(monitor_df), "monitoring_log.csv", "text/csv")
else:
    st.info("Monitoring log not available.")

# --- DETECTION PHASE ---
st.header("⚠️ Detection Phase")
if not detect_df.empty:
    st.dataframe(detect_df.head(10))
    st.bar_chart(detect_df.set_index("file_name")["confidence"])
    st.download_button("📥 Download Detection Data", convert_df(detect_df), "detection_log.csv", "text/csv")
else:
    st.info("Detection log not available.")

# --- QUARANTINE PHASE ---
st.header("🚫 Quarantine Phase")
if not quarantine_df.empty:
    st.dataframe(quarantine_df.head(10))
    st.bar_chart(quarantine_df['classification'].value_counts())
    st.download_button("📥 Download Quarantine Data", convert_df(quarantine_df), "quarantine_log.csv", "text/csv")
else:
    st.info("Quarantine log not available.")

# --- RESOLUTION PHASE ---
st.header("🔧 Resolution Phase")
if not resolution_df.empty:
    st.dataframe(resolution_df.head(10))
    fig, ax = plt.subplots()
    resolution_df['action'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_ylabel("")
    ax.set_title("🔁 Recovery Action Distribution")
    st.pyplot(fig)
    st.download_button("📥 Download Resolution Data", convert_df(resolution_df), "resolution_log.csv", "text/csv")
else:
    st.info("Resolution log not available.")
