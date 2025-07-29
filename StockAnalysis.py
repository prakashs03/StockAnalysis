import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml
import os

st.set_page_config(page_title="Stock Sector Analysis", layout="wide")

# Set the data directory
data_dir = "data"

# ✅ YAML loading block
all_data = []

if not os.path.exists(data_dir):
    st.error("❌ 'data' folder not found. Please upload the extracted YAML folder.")
    st.stop()

for folder_name in os.listdir(data_dir):
    folder_path = os.path.join(data_dir, folder_name)

    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".yaml"):
                file_path = os.path.join(folder_path, filename)

                if not os.path.exists(file_path):
                    continue

                with open(file_path, "r") as file:
                    try:
                        stock_data = yaml.safe_load(file)

                        if isinstance(stock_data, list):
                            for entry in stock_data:
                                if isinstance(entry, dict):
                                    entry["Month"] = folder_name
                                    if "Ticker" in entry:
                                        entry["Symbol"] = entry.pop("Ticker")
                                    all_data.append(entry)

                        elif isinstance(stock_data, dict):
                            stock_data["Month"] = folder_name
                            if "Ticker" in stock_data:
                                stock_data["Symbol"] = stock_data.pop("Ticker")
                            all_data.append(stock_data)

                    except Exception as e:
                        st.warning(f"⚠️ Error reading {file_path}: {e}")

# ✅ Step 1: Debug and verify
st.write(f"✅ Total YAML records loaded: {len(all_data)}")

if len(all_data) > 0:
    st.write("🔍 Sample record from all_data:")
    st.json(all_data[0])
else:
    st.error("❌ No data loaded from YAML files. Check folder structure or file formats.")
    st.stop()

# ✅ Convert to DataFrame
stock_df = pd.DataFrame(all_data)

# ✅ Read sector data
sector_df = pd.read_csv("Sector_data - Sheet1.csv")

# ✅ Clean column names
stock_df.columns = stock_df.columns.str.strip()
sector_df.columns = sector_df.columns.str.strip()

st.write("📌 stock_df columns:", stock_df.columns.tolist())
st.write("📌 sector_df columns:", sector_df.columns.tolist())

# ✅ Confirm Symbol column exists
if "Symbol" not in stock_df.columns:
    st.error("❌ 'Symbol' column is missing in stock_df.")
    st.stop()
if "Symbol" not in sector_df.columns:
    st.error("❌ 'Symbol' column is missing in sector_df.")
    st.stop()

# ✅ Standardize Symbol values
stock_df["Symbol"] = stock_df["Symbol"].astype(str).str.strip().str.upper()
sector_df["Symbol"] = sector_df["Symbol"].astype(str).str.strip().str.upper()

# ✅ Merge
merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")

st.success("✅ Merge successful!")
st.dataframe(merged_df.head())
