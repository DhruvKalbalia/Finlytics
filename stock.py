import streamlit as st;#Streamlit lets you turn Python code into a web app instantly—no frontend needed.
import yfinance as yf;#stock price data from Yahoo Finance
import plotly.express as px;#Plotly Express is a high-level data visualization library that provides a simple and intuitive interface for creating interactive charts and graphs.   

st.title("Finlytics - Stock Price App");
st.sidebar.title("Stock Price App");
ticker_symbol = st.sidebar.text_input("Enter ticker symbol", "AAPL")
start_date = st.sidebar.date_input("Start Date", value = None)
end_date = st.sidebar.date_input("End Date", value = None)

ticker = yf.Ticker(ticker_symbol);
historical_data = ticker.history(start = start_date, end = end_date);

if start_date is not None and end_date is not None:
    #st.write(historical_data);

    st.subheader(f'{ticker_symbol} Closing Price');
    stockData = yf.download(ticker_symbol, start = start_date, end = end_date);
    price_tab, hist_tab, chart_tab = st.tabs(["Price", "Historical Data", "Chart"]);

    with price_tab:
        st.write("Price summary")
        st.write(stockData)
 
    with hist_tab:
        st.write("Historical data")
        st.write(historical_data)

    with chart_tab:
        st.write("Charts")
        y = stockData['Close'].squeeze()
        line_charts = px.line(stockData, stockData.index, y=y, title=ticker_symbol)
        line_charts.update_layout(
        yaxis_title="Closing Price",
        xaxis_title="Date"
        )
        st.plotly_chart(line_charts)

