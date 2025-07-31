import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Stock Analysis Dashboard", layout="wide")
sns.set_style("whitegrid")

# Load data
stock_df = pd.read_csv("final_stock_data.csv")
merged_df = pd.read_csv("final_merged_data.csv")

# Preprocess date
stock_df['date'] = pd.to_datetime(stock_df['date'])
stock_df = stock_df.sort_values(by=['Symbol', 'date'])
stock_df['month'] = stock_df['date'].dt.to_period('M').astype(str)

# --- Tabs ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    " Overview", 
    " Top Gainers/Losers", 
    " Volatility", 
    " Monthly Leaders", 
    " Sector Performance", 
    " Correlation"
])

# --- TAB 1: OVERVIEW ---
with tab1:
    st.header(" Market Summary")

    total_stocks = merged_df['Symbol'].nunique()
    avg_price = merged_df['close'].mean()
    avg_volume = merged_df['volume'].mean()

    yearly_change = stock_df.groupby('Symbol').agg(
        first_price=('close', 'first'),
        last_price=('close', 'last')
    ).reset_index()
    yearly_change['return_pct'] = (yearly_change['last_price'] - yearly_change['first_price']) / yearly_change['first_price'] * 100

    green_stocks = yearly_change[yearly_change['return_pct'] > 0].shape[0]
    red_stocks = yearly_change[yearly_change['return_pct'] < 0].shape[0]

    col1, col2, col3 = st.columns(3)
    col1.metric(" Green Stocks", green_stocks)
    col2.metric(" Red Stocks", red_stocks)
    col3.metric(" Avg Price / Volume", f"{avg_price:.2f} / {avg_volume:,.0f}")

    st.markdown("###  Yearly Return Distribution")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(yearly_change['return_pct'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

# --- TAB 2: GAINERS / LOSERS ---
with tab2:
    st.header(" Top 10 Gainers and Losers")

    yearly_price = stock_df.groupby('Symbol').agg(
        first_close=('close', 'first'),
        last_close=('close', 'last')
    ).reset_index()
    yearly_price['return_pct'] = ((yearly_price['last_close'] - yearly_price['first_close']) / yearly_price['first_close']) * 100

    top_gainers = yearly_price.sort_values(by='return_pct', ascending=False).head(10)
    top_losers = yearly_price.sort_values(by='return_pct', ascending=True).head(10)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("###  Top 10 Gainers")
        st.dataframe(top_gainers)
        fig1, ax1 = plt.subplots()
        sns.barplot(data=top_gainers, x='return_pct', y='Symbol', palette='Greens_r', ax=ax1)
        ax1.set_title('Top 10 Gainers')
        st.pyplot(fig1)

    with col2:
        st.markdown("###  Top 10 Losers")
        st.dataframe(top_losers)
        fig2, ax2 = plt.subplots()
        sns.barplot(data=top_losers, x='return_pct', y='Symbol', palette='Reds_r', ax=ax2)
        ax2.set_title('Top 10 Losers')
        st.pyplot(fig2)

# --- TAB 3: VOLATILITY ---
with tab3:
    st.header(" Volatility Analysis")

    stock_df['daily_return'] = stock_df.groupby('Symbol')['close'].pct_change()
    volatility = stock_df.groupby('Symbol')['daily_return'].std().reset_index()
    volatility.columns = ['Symbol', 'Volatility']
    top_volatility = volatility.sort_values(by='Volatility', ascending=False).head(10)

    st.dataframe(top_volatility)

    fig3, ax3 = plt.subplots()
    sns.barplot(data=top_volatility, x='Volatility', y='Symbol', palette='Oranges_r', ax=ax3)
    ax3.set_title("Top 10 Most Volatile Stocks")
    st.pyplot(fig3)

# --- TAB 4: MONTHLY LEADERS ---
with tab4:
    st.header(" Top 5 Gainers and Losers (Month-wise)")

    monthly_returns = stock_df.groupby(['Symbol', 'month']).agg(
        first_close=('close', 'first'),
        last_close=('close', 'last')
    ).reset_index()
    monthly_returns['return_pct'] = ((monthly_returns['last_close'] - monthly_returns['first_close']) / monthly_returns['first_close']) * 100

    months = sorted(monthly_returns['month'].unique())
    selected_month = st.selectbox("Select a Month", months)

    filtered_month = monthly_returns[monthly_returns['month'] == selected_month]
    top5 = filtered_month.sort_values(by='return_pct', ascending=False).head(5)
    bottom5 = filtered_month.sort_values(by='return_pct', ascending=True).head(5)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"###  Top 5 Gainers - {selected_month}")
        st.dataframe(top5)
        fig4, ax4 = plt.subplots()
        sns.barplot(data=top5, x='return_pct', y='Symbol', palette='Greens_r', ax=ax4)
        st.pyplot(fig4)

    with col2:
        st.markdown(f"###  Top 5 Losers - {selected_month}")
        st.dataframe(bottom5)
        fig5, ax5 = plt.subplots()
        sns.barplot(data=bottom5, x='return_pct', y='Symbol', palette='Reds_r', ax=ax5)
        st.pyplot(fig5)

# --- TAB 5: SECTOR PERFORMANCE ---
with tab5:
    st.header(" Sector-wise Average Returns")

    if 'sector' in merged_df.columns:
        sector_returns = merged_df.groupby('Symbol').agg(
            first_price=('close', 'first'),
            last_price=('close', 'last')
        ).reset_index()
        sector_returns['return_pct'] = ((sector_returns['last_price'] - sector_returns['first_price']) / sector_returns['first_price']) * 100

        sector_info = merged_df[['Symbol', 'sector']].drop_duplicates()
        sector_returns = pd.merge(sector_returns, sector_info, on='Symbol', how='left')
        sector_perf = sector_returns.groupby('sector')['return_pct'].mean().sort_values()

        st.dataframe(sector_perf.reset_index())

        fig6, ax6 = plt.subplots(figsize=(10, 5))
        sns.barplot(x=sector_perf.values, y=sector_perf.index, palette='coolwarm', ax=ax6)
        ax6.set_title("Average Return by Sector")
        st.pyplot(fig6)
    else:
        st.error("Sector data not found in merged_df.")

# --- TAB 6: CORRELATION ---
with tab6:
    st.header(" Stock Price Correlation")

    pivot_df = stock_df.pivot(index='date', columns='Symbol', values='close')
    correlation_matrix = pivot_df.corr()

    st.dataframe(correlation_matrix)

    fig7, ax7 = plt.subplots(figsize=(12, 10))
    sns.heatmap(correlation_matrix, cmap='coolwarm', annot=False, linewidths=0.5, ax=ax7)
    ax7.set_title("Stock Price Correlation Heatmap")
    st.pyplot(fig7)
