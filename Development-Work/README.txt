
==============================
AI-Driven Security Dashboard
==============================

This project provides a web-based dashboard to visualize logs and insights from an AI-Driven Adaptive Security and Recovery Pipeline using Streamlit.

------------------------------
📦 Prerequisites
------------------------------
- Windows/Linux/Mac OS
- Python 3.7 or higher

------------------------------
🔧 Installation Steps
------------------------------

1. Check if Python is installed:
   Open Command Prompt and run:
   python --version

   If not installed, download from:
   https://www.python.org/downloads/

   IMPORTANT: During installation, check the box "Add Python to PATH".

2. Install required Python libraries:
   Open Command Prompt and run:

   pip install streamlit pandas matplotlib

3. Place the following files in one folder:
   - dashboard.py (this script)
   - monitoring_log.csv
   - detection_log.csv
   - quarantine_log.csv
   - resolution_log.csv

4. Navigate to that folder in Command Prompt:

   cd path\to\your\dashboard\folder

5. Run the dashboard:

   streamlit run dashboard.py

6. A browser window will automatically open with the live dashboard UI.
   If not, visit: http://localhost:8501

------------------------------
📂 Files Used
------------------------------
- monitoring_log.csv       : Output of Monitoring phase
- detection_log.csv        : Output of Detection phase
- quarantine_log.csv       : Output of Quarantine phase
- resolution_log.csv       : Output of Resolution phase
- dashboard.py             : The Streamlit dashboard code
- README.txt               : Setup instructions

------------------------------
📝 Notes
------------------------------
- The dashboard includes download buttons for exporting CSV logs.
- Timeline anomaly trend is visualized for better insight.
- Confidence and threat classification are graphed.
- Recovery actions are displayed via a pie chart.

------------------------------
📬 Support
------------------------------
If you need help, contact your project supervisor or visit https://docs.streamlit.io/
