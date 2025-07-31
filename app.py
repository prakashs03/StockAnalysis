# STEP 1: Calculate Yearly Return + Top Gainers and Losers
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sqlalchemy import create_engine

# PostgreSQL connection
host = "localhost"
port = "5432"
database = "stock__analysis"
user = "postgre"
password = "root"
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

# Load data from PostgreSQL
stock_df = pd.read_sql("SELECT * FROM stock_data", engine)
merged_df = pd.read_sql("SELECT * FROM merged_data", engine)

# Ensure 'date' column is datetime
df = stock_df.copy()
df['date'] = pd.to_datetime(df['date'])

# Sort data just in case
df = df.sort_values(by=['Symbol', 'date'])

# Calculate yearly return per stock
yearly_price = df.groupby('Symbol').agg(first_close=('close', 'first'), last_close=('close', 'last')).reset_index()
yearly_price['return_pct'] = ((yearly_price['last_close'] - yearly_price['first_close']) / yearly_price['first_close']) * 100

# Top 10 gainers and losers
top_gainers = yearly_price.sort_values(by='return_pct', ascending=False).head(10)
top_losers = yearly_price.sort_values(by='return_pct', ascending=True).head(10)

# Show in Streamlit
st.subheader("📈 Top 10 Gaining Stocks (Yearly Return %)")
st.dataframe(top_gainers)

st.subheader("📉 Top 10 Losing Stocks (Yearly Return %)")
st.dataframe(top_losers)

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=top_gainers, x='return_pct', y='Symbol', palette='Greens_r', ax=ax)
ax.set_title('Top 10 Gainers')
ax.set_xlabel('Yearly Return (%)')
st.pyplot(fig)

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(data=top_losers, x='return_pct', y='Symbol', palette='Reds_r', ax=ax2)
ax2.set_title('Top 10 Losers')
ax2.set_xlabel('Yearly Return (%)')
st.pyplot(fig2)

# STEP 5: Top 5 Gainers and Losers (Month-wise)
# Group by Symbol + Month
df['month'] = df['date'].dt.to_period('M').astype(str)

# Get first and last close prices per Symbol per Month
monthly_returns = df.groupby(['Symbol', 'month']).agg(
    first_close=('close', 'first'),
    last_close=('close', 'last')
).reset_index()

# Calculate monthly return %
monthly_returns['return_pct'] = (
    (monthly_returns['last_close'] - monthly_returns['first_close']) / monthly_returns['first_close']
) * 100

# Displaying results in Streamlit
st.subheader(" Top 5 Gainers and Losers Per Month")
months = monthly_returns['month'].unique()
selected_month = st.selectbox("Select a month:", sorted(months))

monthly_filtered = monthly_returns[monthly_returns['month'] == selected_month]
top5 = monthly_filtered.sort_values(by='return_pct', ascending=False).head(5)
bottom5 = monthly_filtered.sort_values(by='return_pct', ascending=True).head(5)

col1, col2 = st.columns(2)

with col1:
    st.markdown("###  Top 5 Gainers")
    st.dataframe(top5)
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=top5, x='return_pct', y='Symbol', palette='Greens_r', ax=ax3)
    ax3.set_title(f"Top 5 Gainers - {selected_month}")
    st.pyplot(fig3)

with col2:
    st.markdown("###  Top 5 Losers")
    st.dataframe(bottom5)
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=bottom5, x='return_pct', y='Symbol', palette='Reds_r', ax=ax4)
    ax4.set_title(f"Top 5 Losers - {selected_month}")
    st.pyplot(fig4)

# STEP 6: Optional SQL Query Tab
st.subheader(" Run Custom SQL Query")
user_query = st.text_area("Enter your SQL query:")
if st.button("Run Query"):
    try:
        result_df = pd.read_sql(user_query, engine)
        st.dataframe(result_df)
    except Exception as e:
        st.error(f" Error: {e}")
