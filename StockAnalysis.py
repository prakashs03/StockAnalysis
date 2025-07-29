#!/usr/bin/env python
# coding: utf-8
import streamlit as st
import zipfile
import os

# Unzip if needed
if not os.path.exists("data") and os.path.exists("data.zip"):
    with zipfile.ZipFile("data.zip", "r") as zip_ref:
        zip_ref.extractall(".")

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Packages loaded successfully!")


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


df = pd.read_csv("Sector_data - Sheet1.csv")

# Show the first few rows
df.head()


# In[10]:


import pandas as pd

df = pd.read_csv("Sector_data - Sheet1.csv")
df.head()


# In[8]:


import os
print(os.getcwd())


# In[9]:


import os
print(os.listdir())


# In[12]:


import pandas as pd

df = pd.read_csv("Sector_data - Sheet1.csv")
df.head()


# In[13]:


# Check first few rows
df.head()


# In[14]:


# Check info about the dataset
df.info()

# Summary statistics for numbers
df.describe()

# Check for any missing values
df.isnull().sum()




# In[3]:


import os
import yaml
import pandas as pd

# Path to the main "data" folder
data_dir = "data"


# Store results here
all_data = []

# Loop through each folder (like 'May 2023', 'June 2023')
for folder_name in os.listdir(data_dir):
    folder_path = os.path.join(data_dir, folder_name)

    # Make sure it's a folder (skip any files)
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".yaml"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r') as file:
                    try:
                        stock_data = yaml.safe_load(file)
                        # Add the month info from folder
                        stock_data['Month'] = folder_name
                        all_data.append(stock_data)
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

# Convert to DataFrame
stock_df = pd.DataFrame(all_data)
stock_df.head()


# In[4]:


print("Number of records loaded:", len(stock_df))


# In[5]:


import os
import yaml
import pandas as pd

# STEP 1: Set your folder path
data_dir = "data"   # Change if different

# STEP 2: Load all .yaml files into one list
all_data = []

for filename in os.listdir(data_dir):
    if filename.endswith(".yaml"):
        file_path = os.path.join(data_dir, filename)
        with open(file_path, 'r') as file:
            try:
                content = yaml.safe_load(file)
                all_data.append(content)
            except Exception as e:
                print(f"Error loading {filename}: {e}")

# STEP 3: Convert to DataFrame
stock_df = pd.DataFrame(all_data)
stock_df.head()


# In[6]:


import os
import yaml
import pandas as pd

# Path to the main folder containing all month folders
data_dir = "data"

# Store all YAML records
all_data = []

# Recursively walk through all subfolders and read YAML files
for root, dirs, files in os.walk(data_dir):
    for filename in files:
        if filename.endswith(".yaml"):
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'r') as f:
                    content = yaml.safe_load(f)
                    content['Source File'] = filename
                    all_data.append(content)
            except Exception as e:
                print(f"Error in {file_path}: {e}")

# Convert to DataFrame
stock_df = pd.DataFrame(all_data)

# Show result
print("✅ Total YAML records loaded:", len(stock_df))
stock_df.head()


# In[7]:


import yaml

with open(file_path, 'r') as f:
    content = yaml.safe_load(f)

print(type(content))
print(content)


# In[8]:


import pandas as pd

stock_df = pd.DataFrame(all_data)
stock_df.head()


# In[9]:


stock_df.rename(columns={"Ticker": "Symbol"}, inplace=True)


# In[11]:


sector_df = pd.read_csv("Sector_data - Sheet1.csv")
sector_df.head()

# Read the CSV (correct name and path)
sector_df = pd.read_csv("Sector_data - Sheet1.csv")

# Clean column names
stock_df.columns = stock_df.columns.str.strip()
sector_df.columns = sector_df.columns.str.strip()

# Capitalize all values in Symbol column
stock_df['Symbol'] = stock_df['Symbol'].astype(str).str.strip().str.upper()
sector_df['Symbol'] = sector_df['Symbol'].astype(str).str.strip().str.upper()

# Confirm existence before merge
st.write("stock_df columns:", stock_df.columns.tolist())
st.write("sector_df columns:", sector_df.columns.tolist())

if "Symbol" not in stock_df.columns or "Symbol" not in sector_df.columns:
    st.error("❌ 'Symbol' column missing. Please check your file structure.")
    st.stop()

# Merge safely
merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")

# In[12]:

st.write("✅ stock_df columns:", stock_df.columns.tolist())
st.write("✅ sector_df columns:", sector_df.columns.tolist())

if "Symbol" not in stock_df.columns:
    st.error("❌ 'Symbol' column is missing in stock_df")
    st.stop()
    
if "Symbol" not in sector_df.columns:
    st.error("❌ 'Symbol' column is missing in sector_df")
    st.stop()

merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")
merged_df.head()


# In[13]:


print("stock_df columns:", stock_df.columns.tolist())


# In[14]:


print("Number of records:", len(all_data))
print("First record:", all_data[0])


# In[15]:


import os
import yaml

data_dir = "data"
all_data = []

if not os.path.exists(data_dir):
    st.error("❌ 'data' folder not found.")
    st.stop()

for folder_name in os.listdir(data_dir):
    folder_path = os.path.join(data_dir, folder_name)

    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".yaml"):
                file_path = os.path.join(folder_path, filename)

                if not os.path.exists(file_path):
                    continue

                with open(file_path, 'r') as file:
                    try:
                        stock_data = yaml.safe_load(file)

                        if isinstance(stock_data, list):
                            for entry in stock_data:
                                if isinstance(entry, dict):
                                    entry['Month'] = folder_name
                                    all_data.append(entry)
                        elif isinstance(stock_data, dict):
                            stock_data['Month'] = folder_name
                            all_data.append(stock_data)
                    except Exception as e:
                        st.warning(f"⚠️ Error reading {file_path}: {e}")

# In[16]:


import pandas as pd

stock_df = pd.DataFrame(all_data)
stock_df.head()


# In[17]:


stock_df.rename(columns={'Ticker': 'Symbol'}, inplace=True)


# In[30]:


sector_df = pd.read_csv("Sector_data - Sheet1.csv")

# Strip unwanted spaces from all column names
stock_df.columns = stock_df.columns.str.strip()
sector_df.columns = sector_df.columns.str.strip()

# Standardize 'Symbol' values to uppercase, no whitespace
if "Symbol" in stock_df.columns:
    stock_df['Symbol'] = stock_df['Symbol'].astype(str).str.strip().str.upper()
else:
    st.error("❌ 'Symbol' column missing in stock_df.")
    st.stop()

if "Symbol" in sector_df.columns:
    sector_df['Symbol'] = sector_df['Symbol'].astype(str).str.strip().str.upper()
else:
    st.error("❌ 'Symbol' column missing in sector_df.")
    st.stop()

# Merge both DataFrames using Symbol
merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")

# Show sample
st.write("✅ Sample merged data:")
st.dataframe(merged_df.head())


# In[19]:


print("Symbols from stock_df:")
print(stock_df["Symbol"].unique()[:10])

print("\nSymbols from sector_df:")
print(sector_df["Symbol"].unique()[:10])


# In[20]:


# Split the column into Company Name and Symbol
sector_df[['COMPANY', 'Symbol']] = sector_df['Symbol'].str.split(':', expand=True)

# Strip spaces and make uppercase
sector_df['COMPANY'] = sector_df['COMPANY'].str.strip()
sector_df['Symbol'] = sector_df['Symbol'].str.strip().str.upper()


# In[21]:


print(sector_df.head())


# In[22]:


merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")
merged_df.head()


# In[23]:


print("Still missing sectors?", merged_df['sector'].isnull().sum())


# In[24]:


# Show all unique symbols that didn’t match
unmatched = merged_df[merged_df['sector'].isnull()]
print(unmatched['Symbol'].unique())


# In[25]:


additional_mappings = pd.DataFrame({
    "COMPANY": ["TATA CONSUMER", "BHARTI AIRTEL", "ADANI ENTERPRISES", "BRITANNIA"],
    "sector": ["FMCG", "Telecom", "Conglomerate", "FMCG"],
    "Symbol": ["TATACONSUM", "BHARTIARTL", "ADANIENT", "BRITANNIA"]
})

# Append and re-merge
sector_df = pd.concat([sector_df, additional_mappings], ignore_index=True)

# Merge again
merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")
merged_df = merged_df.dropna(subset=["sector", "COMPANY"])


# In[26]:


print("Still missing sectors?", merged_df['sector'].isnull().sum())


# In[27]:


import matplotlib.pyplot as plt

avg_close = merged_df.groupby("sector")["close"].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
avg_close.plot(kind='bar', color='skyblue')
plt.title("Average Closing Price by Sector")
plt.xlabel("Sector")
plt.ylabel("Average Close Price")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# In[28]:


# Create volatility column
merged_df["volatility"] = merged_df["high"] - merged_df["low"]

# Top 10 most volatile stock entries (by day)
top_volatility = merged_df.sort_values(by="volatility", ascending=False).head(10)

top_volatility[["Symbol", "COMPANY", "sector", "date", "volatility"]]


# In[29]:


sector_volume = merged_df.groupby("sector")["volume"].sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
sector_volume.plot(kind='bar', color='orange')
plt.title("Total Volume Traded by Sector")
plt.xlabel("Sector")
plt.ylabel("Total Volume")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# In[31]:


sector_df = pd.read_csv("sector_data - sheet1.csv")

# Strip any unwanted spaces from column names
sector_df.columns = sector_df.columns.str.strip()

# Merge both DataFrames using Symbol
merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")

# Show sample
merged_df.head()


# In[32]:


print(sector_df.columns.tolist())


# In[33]:


# Clean Symbol in stock_df
stock_df["Symbol"] = stock_df["Symbol"].astype(str).str.strip().str.upper()

# Clean Symbol in sector_df
sector_df["Symbol"] = sector_df["Symbol"].astype(str).str.strip().str.upper()


# In[34]:


merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")


# In[35]:


# Check if sectors are now populated
print("Missing sectors after merge:", merged_df['sector'].isnull().sum())

# Show a few rows to confirm
merged_df.head()


# In[36]:


print("From stock_df:", stock_df['Symbol'].unique()[:10])
print("From sector_df:", sector_df['Symbol'].unique()[:10])


# In[37]:


# Split 'COMPANY: SYMBOL' into two new columns
sector_df[['COMPANY', 'Symbol']] = sector_df['Symbol'].str.split(':', expand=True)

# Clean up spaces and capitalization
sector_df['COMPANY'] = sector_df['COMPANY'].str.strip()
sector_df['Symbol'] = sector_df['Symbol'].str.strip().str.upper()


# In[38]:


stock_df['Symbol'] = stock_df['Symbol'].astype(str).str.strip().str.upper()


# In[39]:


merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")

print("Missing sectors after merge:", merged_df['sector'].isnull().sum())
merged_df.head()


# In[40]:


# Add missing mappings manually
new_entries = pd.DataFrame({
    "COMPANY": ["TITAN COMPANY", "ITC LTD", "RELIANCE INDUSTRIES", "JSW STEEL", "HCL TECHNOLOGIES", "L&T", "TATA CONSUMER"],
    "sector": ["Consumer Goods", "FMCG", "Energy", "Metals", "IT", "Infrastructure", "FMCG"],
    "Symbol": ["TITAN", "ITC", "RELIANCE", "JSWSTEEL", "HCLTECH", "LT", "TATACONSUM"]
})

# Append to sector_df
sector_df = pd.concat([sector_df, new_entries], ignore_index=True)

# Re-merge
merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")
print("✅ Missing sectors after final merge:", merged_df["sector"].isnull().sum())


# In[41]:


# Example — replace with your actual missing symbols and correct values
extra_mappings = pd.DataFrame({
    "COMPANY": [
        "TATA CONSUMER PRODUCTS", "BHARTI AIRTEL", "ADANI ENTERPRISES", "BRITANNIA INDUSTRIES",
        "INFOSYS", "ULTRATECH CEMENT", "SUN PHARMA", "NTPC", "NESTLE INDIA"
        # Add more as needed...
    ],
    "sector": [
        "FMCG", "Telecom", "Conglomerate", "FMCG",
        "IT", "Cement", "Pharmaceuticals", "Energy", "FMCG"
        # Match the sectors correctly...
    ],
    "Symbol": [
        "TATACONSUM", "BHARTIARTL", "ADANIENT", "BRITANNIA",
        "INFY", "ULTRACEMCO", "SUNPHARMA", "NTPC", "NESTLEIND"
        # These should match missing_symbols exactly
    ]
})


# In[42]:


# Append to existing sector_df
sector_df = pd.concat([sector_df, extra_mappings], ignore_index=True)


# In[43]:


merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")

# Check again
print("✅ Missing sectors after full merge:", merged_df['sector'].isnull().sum())


# In[44]:


merged_df = pd.merge(stock_df, sector_df, on="Symbol", how="left")

print("Missing sectors after merge:", merged_df['sector'].isnull().sum())
merged_df.head()


# In[45]:


import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")


# In[46]:


plt.figure(figsize=(12,6))
avg_close = merged_df.groupby("sector")["close"].mean().sort_values(ascending=False)
sns.barplot(x=avg_close.values, y=avg_close.index, palette="coolwarm")

plt.title("Average Closing Price by Sector", fontsize=14)
plt.xlabel("Average Close Price")
plt.ylabel("Sector")
plt.tight_layout()
plt.show()


# In[48]:


# Rebuild as DataFrame for clarity
avg_close_df = avg_close.reset_index()
avg_close_df.columns = ['sector', 'average_close']

plt.figure(figsize=(12,6))
sns.barplot(
    data=avg_close_df,
    x='average_close',
    y='sector',
    palette="coolwarm",
    hue=None,
    legend=False
)


plt.title("Average Closing Price by Sector", fontsize=14)
plt.xlabel("Average Close Price")
plt.ylabel("Sector")
plt.tight_layout()
plt.show()


# In[49]:


# Prepare data
avg_close_df = avg_close.reset_index()
avg_close_df.columns = ['sector', 'average_close']

plt.figure(figsize=(12, 6))
sns.barplot(
    data=avg_close_df,
    x='average_close',
    y='sector',
    color='skyblue'  # use a single color instead of a palette
)

plt.title("Average Closing Price by Sector", fontsize=14)
plt.xlabel("Average Close Price")
plt.ylabel("Sector")
plt.tight_layout()
plt.show()


# In[50]:


# Total Volume Traded by Sector
sector_volume = merged_df.groupby("sector")["volume"].sum().sort_values(ascending=False)
sector_volume_df = sector_volume.reset_index()
sector_volume_df.columns = ['sector', 'total_volume']

plt.figure(figsize=(12,6))
sns.barplot(
    data=sector_volume_df,
    x='total_volume',
    y='sector',
    color='lightgreen'  # Single color to avoid warning
)

plt.title("Total Volume Traded by Sector", fontsize=14)
plt.xlabel("Total Volume")
plt.ylabel("Sector")
plt.tight_layout()
plt.show()


# In[51]:


# Calculate daily volatility
merged_df["volatility"] = merged_df["high"] - merged_df["low"]

# Get average volatility per company
top_volatility = (
    merged_df.groupby("COMPANY")["volatility"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# Prepare for plotting
volatility_df = top_volatility.reset_index()
volatility_df.columns = ['COMPANY', 'average_volatility']

plt.figure(figsize=(12,6))
sns.barplot(
    data=volatility_df,
    x='average_volatility',
    y='COMPANY',
    color='salmon'
)

plt.title("Top 10 Most Volatile Stocks", fontsize=14)
plt.xlabel("Average Daily Volatility (High - Low)")
plt.ylabel("Company")
plt.tight_layout()
plt.show()


# In[52]:


# Average Close Price by Company
top_close = (
    merged_df.groupby("COMPANY")["close"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# Prepare for plotting
top_close_df = top_close.reset_index()
top_close_df.columns = ['COMPANY', 'average_close']

plt.figure(figsize=(12,6))
sns.barplot(
    data=top_close_df,
    x='average_close',
    y='COMPANY',
    color='lightblue'
)

plt.title("Top 10 Companies by Average Close Price", fontsize=14)
plt.xlabel("Average Close Price")
plt.ylabel("Company")
plt.tight_layout()
plt.show()


# In[ ]:




