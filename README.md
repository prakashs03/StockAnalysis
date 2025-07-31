# 📊 Stock Market Analysis and Dashboard

An end-to-end project that performs data extraction, transformation, analysis, visualization, and dashboard deployment for stock market data using **Python**, **PostgreSQL**, **Power BI**, and **Streamlit**.

---

## 🧾 Project Overview

This project aims to analyze NIFTY 50 stock data provided in YAML format. It includes:

- Data extraction and cleaning from YAML files
- Monthly and yearly return calculations
- Top gainers/losers analysis
- Sector-wise performance
- Volatility analysis
- Correlation heatmap
- Interactive dashboards using **Streamlit**
- Visualizations in **Power BI**
- Uploading final data to **PostgreSQL**

---

## 📁 Folder Structure

```
├── data/                         # Contains YAML files organized by month
├── final_stock_data.csv         # Processed stock data
├── final_merged_data.csv        # Stock + Sector merged data
├── StockAnalysis.ipynb          # Jupyter notebook with all analysis steps
├── app.py                       # Streamlit dashboard app
├── upload_to_postgres.py        # Script to upload data to PostgreSQL
├── requirements.txt             # List of required Python libraries
└── README.md                    # Project documentation
```

---

## 🚀 Features

### ✅ Data Analysis

- Top 10 yearly gainers and losers
- Monthly Top 5 gainers and losers
- Sector-wise average return
- Volatility of top stocks
- Stock correlation heatmap

### 📈 Visualizations

- Built using **Matplotlib**, **Seaborn**, and **Power BI**
- Dashboard for quick insights

### 🌐 Web Dashboard

- Interactive interface using **Streamlit**
- Filters for sector, symbol, and date

### 🛢️ Database Integration

- Final CSV files uploaded to **PostgreSQL**
- Tables:
  - `public.stock_data`
  - `public.merged_data`

---

## 🧰 Technologies Used

| Tool | Purpose |
|------|---------|
| **Python** | Core data analysis |
| **Pandas, NumPy** | Data handling and processing |
| **Seaborn, Matplotlib** | Visualizations |
| **Streamlit** | Web dashboard |
| **Power BI** | Business intelligence and charts |
| **PostgreSQL** | SQL database |
| **SQLAlchemy** | Python-SQL connection |
| **YAML** | Raw data format |

---

## 🗃️ Setup Instructions

### 1️⃣ Clone this Repository

```bash
git clone https://github.com/yourusername/stock-market-analysis.git
cd stock-market-analysis
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

### 4️⃣ Load Data to PostgreSQL

Edit `upload_to_postgres.py` with your DB credentials:

```python
engine = create_engine("postgresql://username:password@localhost:5432/your_db")
```

Then run:

```bash
python upload_to_postgres.py
```

---

## 📦 Requirements

See [requirements.txt](./requirements.txt)

---

## 🖥️ Power BI Report

- Open Power BI Desktop
- Connect to `PostgreSQL`
- Import `merged_data` table
- Create visuals for:
  - Top Gainers/Losers
  - Sector-wise returns
  - Volatility
  - Monthly gainers
  - Correlation matrix

---

## 📌 Future Scope

- Real-time data fetching using APIs
- Predictive analytics using ML models
- Deployment with Docker

---

## 📝 Author

Jayaprakash Srinivasan  
📧 jayaprakash.email@example.com  
📍 Tamil Nadu, India

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.