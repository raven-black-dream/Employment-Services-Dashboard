# Employment Services in BC - Streamlit Dashboard

This project is an interactive web dashboard built with Streamlit to visualize and analyze data related to Employment Services in British Columbia. It provides at-a-glance metrics, trend plots, and detailed data tables.

## 📊 Features

The dashboard is organized into three main sections:

### 1. Key Metrics

This section provides a high-level overview of the most recent year's performance (hardcoded to 2023) with a comparison (delta) to the prior year.
* **Case Counts by Plan Status:**
    * Open Cases
    * Closed Cases
* **Case Counts by Service Status:**
    * Set Up
    * Waiting to Start
    * In Progress
    * Ended Delivery
    * Closed
    * Cancelled
* **Annual Costs:**
    * Total Costs
    * Outcome Fees Paid
    * Service Support Costs

### 2. Basic Plots

This section displays interactive line charts to visualize trends over time.
* **Monthly Total Cost by Plan Name:** A line chart showing the total cost per month, categorized by the service plan name.
* **Monthly Count of Cases by Gender:** A line chart showing the number of cases per month, categorized by gender.

### 3. Data Tables

This section presents pivot tables that provide aggregated annual counts for deeper analysis.
* **Annual Count of Cases by Education Level**
* **Annual Count of Cases by Service/Subservice**
* **Annual Count of Cases by Client Type**

## ⚙️ Prerequisites

Before you run this application, you need to have Python installed along with the following libraries:
* **streamlit**
* **pandas**
* **plotly**
* **openpyxl** (required by pandas to read `.xlsx` files)

You will also need a data file named `data.xlsx` located in the same directory as the script.

## 📦 Installation

1.  **Clone or download the repository/script.**
2.  **Install the required libraries** using pip:
    ```bash
    pip install streamlit pandas plotly openpyxl
    ```
3.  **Place your data file** named `data.xlsx` in the root directory of the project. The file must contain the following columns:
    * `SERVICE_START_DATE` (datetime format)
    * `SRV_PLAN_STATUS_CD`
    * `SERVICE_STATUS_CD`
    * `TOTAL_COST_AMT`
    * `OUTCOME_FEES_PAID_AMT`
    * `SERVICE_SUPPORT_COST_AMT`
    * `PLAN_NAME`
    * `GENDER`
    * `EDUCATION_LEVEL`
    * `SERVICE`
    * `SUB_SERVICE`
    * `CASE_NUM`
    * `CLIENT_TYPE`

## ▶️ How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you saved the Python script and the `data.xlsx` file.
3.  Run the following command:
    ```bash
    streamlit run your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file).

Your web browser will automatically open a new tab with the running Streamlit application.
