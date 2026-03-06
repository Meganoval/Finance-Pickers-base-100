import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("📈 Performance Base 100 depuis 2016")

tickers = st.text_input(
    "Tickers Yahoo Finance (ex: NVDA, AAPL, BTC-USD, ^GSPC)"
)

if tickers:

    fig = go.Figure()

    for t in tickers.split(","):
        t = t.strip().upper()

        df = yf.download(
            t,
            start="2016-01-01",
            progress=False,
            auto_adjust=True
        )

        if df.empty:
            continue

        base100 = df["Close"] / df["Close"].iloc[0] * 100

        fig.add_trace(
            go.Scatter(
                x=base100.index,
                y=base100,
                mode="lines",
                name=t
            )
        )

    fig.update_layout(
        hovermode="x unified",
        height=650,
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)
