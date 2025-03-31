import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Initialize Streamlit App
st.set_page_config(page_title="Rationites - Stock Analysis", layout="wide")
st.title("📊 Rationites - Smarter Stock Analysis")

# User Input for Stock Symbol
stock_symbol = st.text_input("Enter a stock symbol (e.g., TSLA, AAPL):").upper()

# Store time range in session state
if "time_range" not in st.session_state:
    st.session_state["time_range"] = "1 Year"

time_range = st.selectbox(
    "Select Time Range",
    ["1 Year", "6 Months", "1 Month", "7 Days"],
    index=["1 Year", "6 Months", "1 Month", "7 Days"].index(st.session_state["time_range"])
)
st.session_state["time_range"] = time_range  # Persist selection

def fetch_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period="1y")
        if df.empty:
            return None
        df.reset_index(inplace=True)
        return df
    except Exception as e:
        st.error(f"Error fetching stock data: {e}")
        return None

def fetch_financial_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        financials = stock.financials.transpose()
        if financials.empty:
            return None
        financials = financials[["Total Revenue", "Net Income"]]
        financials.reset_index(inplace=True)
        financials.rename(columns={"index": "Year"}, inplace=True)
        return financials
    except Exception as e:
        st.error(f"Error fetching financial data: {e}")
        return None

if st.button("Analyze Stock"):
    if stock_symbol:
        stock_data = fetch_stock_data(stock_symbol)
        financial_data = fetch_financial_data(stock_symbol)

        if stock_data is not None:
            # Filter data based on selected time range
            days_map = {"1 Year": 365, "6 Months": 180, "1 Month": 30, "7 Days": 7}
            stock_data = stock_data.tail(days_map[time_range])

            # Plot interactive stock price chart
            st.subheader(f"Market Value of {stock_symbol} Over Time")
            fig = px.line(stock_data, x="Date", y="Close", title=f"{stock_symbol} Market Price",
                          labels={"Date": "Date", "Close": "Closing Price (USD)"},
                          template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("⚠️ Stock not found! Please check the symbol and try again.")

        if financial_data is not None:
            st.subheader("Revenue vs Net Income Over the Years")
            fig = go.Figure()
            fig.add_trace(go.Bar(x=financial_data["Year"], y=financial_data["Total Revenue"], name="Revenue", marker_color="blue"))
            fig.add_trace(go.Bar(x=financial_data["Year"], y=financial_data["Net Income"], name="Net Income", marker_color="green"))
            fig.update_layout(barmode="group", title="Revenue vs Net Income Over the Years")
            st.plotly_chart(fig)
        else:
            st.error("⚠️ Financial data not available.")
