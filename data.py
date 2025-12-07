import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff

st.set_page_config(page_title="Multi Dashboard", layout="wide")

# ---- SIDEBAR MENU ----
menu = st.sidebar.radio(
    "📌 Select Dashboard",
    ["Home", "Gain and Loose Stock", "Volatility", "Cummulative","Average_Yearly","Correlated_Heatmap","Monthly_Return"]
)

if menu == "Home":
    st.title("📈 Top 10 Stock Performance Dashboard")
    
    @st.cache_data
    def load_data():
        return pd.read_csv("data.csv")
    
    df = load_data()
    
    st.subheader("Full Dataset Columns")
    st.write(df.columns.tolist())   # Shows all columns in your CSV
    
    # Find numeric columns automatically
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    st.subheader("Numeric Columns Detected")
    st.write(numeric_columns)
    
    # Dropdown to select performance column
    performance_column = st.selectbox("Select performance column:", numeric_columns)
    
    # Compute top 10 based on selected column
    top10 = df.sort_values(by=performance_column, ascending=False).head(10)
    
    st.subheader("🏆 Top 10 Performing Stocks")
    st.dataframe(top10)
    
    # Optional: bar chart
    if len(top10) > 0:
        st.subheader("📊 Performance Chart")
    
        # find first non-numeric column → usually stock name
        text_columns = df.select_dtypes(exclude=['float64', 'int64']).columns.tolist()
    
        if len(text_columns) == 0:
            st.error("No text column available to use as stock names.")
        else:
            index_col = text_columns[0]
            st.bar_chart(top10.set_index(index_col)[performance_column])
    
## Top 10 Green Stocks
elif menu == "Gain and Loose Stock":
    st.title("Top 10 Green Stock")
    
    @st.cache_data
    def load_data():
        return pd.read_csv("Green.csv")
    
    df = load_data()
    
    st.subheader("Full Dataset Columns")
    st.write(df.columns.tolist())   # Shows all columns in your CSV
    
    # Find numeric columns automatically
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    st.subheader("Numeric Columns Detected")
    st.write(numeric_columns)
    
    # Dropdown to select performance column
    performance_column = st.selectbox(
        "Select performance column:",
        numeric_columns,
        key="performance_column_selectbox"
    )
    
    
    # Compute top 10 based on selected column
    top10 = df.sort_values(by=performance_column, ascending=False).head(10)
    
    st.subheader("🏆 Top 10 Performing  Green Stocks")
    st.dataframe(top10)
    
    # Visual Bar Chart with Green Color
    if len(top10) > 0:
        st.subheader("📊 Performance Chart (Green Bars)")
    
        # find first non-numeric column → usually stock name
        text_columns = df.select_dtypes(exclude=['float64', 'int64']).columns.tolist()
    
        if len(text_columns) == 0:
            st.error("No text column available to use as stock names.")
        else:
            index_col = text_columns[0]
    
            chart = (
                alt.Chart(top10)
                .mark_bar(color="green")
                .encode(
                    x=alt.X(index_col, sort=None),
                    y=performance_column
                )
                .properties(width=600, height=400)
            )
    
            st.altair_chart(chart, use_container_width=True)
    
    ## Top 10 Red Stock 
    
    
    st.title("Top 10 Red Stock")
    
    @st.cache_data
    def load_data():
        return pd.read_csv("Red.csv")
    
    df = load_data()
    
    st.subheader("Full Dataset Columns")
    st.write(df.columns.tolist())   # Shows all columns in your CSV
    
    # Find numeric columns automatically
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    st.subheader("Numeric Columns Detected")
    st.write(numeric_columns)
    
    # Dropdown to select performance column
    performance_column = st.selectbox("Select performance column:", numeric_columns)
    
    # Compute top 10 based on selected column
    top10 = df.sort_values(by=performance_column, ascending=False).head(10)
    
    st.subheader("🏆 Top 10 Red Stocks")
    st.dataframe(top10)
    
    # Visual Bar Chart with Green Color
    if len(top10) > 0:
        st.subheader("📊 Performance Chart (Red Bars)")
    
        # find first non-numeric column → usually stock name
        text_columns = df.select_dtypes(exclude=['float64', 'int64']).columns.tolist()
    
        if len(text_columns) == 0:
            st.error("No text column available to use as stock names.")
        else:
            index_col = text_columns[0]
    
            chart = (
                alt.Chart(top10)
                .mark_bar(color="red")
                .encode(
                    x=alt.X(index_col, sort=None),
                    y=performance_column
                )
                .properties(width=600, height=400)
            )
    
            st.altair_chart(chart, use_container_width=True)
    
     ## Average Price by Green Stock
    
    st.title("Top  Average Price of Green Stock")
    
    @st.cache_data
    def load_data():
        return pd.read_csv("Average _Price _by _Green _Stock.csv")
    
    df = load_data()
    
    st.subheader("Full Dataset Columns")
    st.write(df.columns.tolist())   # Shows all columns in your CSV
    
    # Find numeric columns automatically
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    st.subheader("Numeric Columns Detected")
    st.write(numeric_columns)
    
    # Dropdown to select performance column
    performance_column = st.selectbox(
        "Select performance column",
        options=df.columns,
        key="performance_column_selectbox_1"
    )
    
    
    # Compute top 10 based on selected column
    top10 = df.sort_values(by=performance_column, ascending=False).head(10)
    
    st.subheader("🏆 Top 10 Performing  Green Stocks")
    st.dataframe(top10)
    
    # Visual Bar Chart with Green Color
    if len(top10) > 0:
        st.subheader("📊 Performance Chart (Green Bars)")
    
        # find first non-numeric column → usually stock name
        text_columns = df.select_dtypes(exclude=['float64', 'int64']).columns.tolist()
    
        if len(text_columns) == 0:
            st.error("No text column available to use as stock names.")
        else:
            index_col = text_columns[0]
    
            chart = (
                alt.Chart(top10)
                .mark_bar(color="green")
                .encode(
                    x=alt.X(index_col, sort=None),
                    y=performance_column
                )
                .properties(width=600, height=400)
            )
    
            st.altair_chart(chart, use_container_width=True)
    
    ## Average Price by Red Stock
    
    st.title("Top 10 Average Price of Red Stock")
    
    @st.cache_data
    def load_data():
        return pd.read_csv("Average_Price_by_Red_Stock.csv")
    
    df = load_data()
    
    st.subheader("Full Dataset Columns")
    st.write(df.columns.tolist())   # Shows all columns in your CSV
    
    # Find numeric columns automatically
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    st.subheader("Numeric Columns Detected")
    st.write(numeric_columns)
    
    # Dropdown to select performance column
    performance_column = st.selectbox("Select performance column:", numeric_columns)
    
    # Compute top 10 based on selected column
    top10 = df.sort_values(by=performance_column, ascending=False).head(10)
    
    st.subheader("🏆 Top 10 Red Stocks")
    st.dataframe(top10)
    
    # Visual Bar Chart with Green Color
    if len(top10) > 0:
        st.subheader("📊 Performance Chart (Red Bars)")
    
        # find first non-numeric column → usually stock name
        text_columns = df.select_dtypes(exclude=['float64', 'int64']).columns.tolist()
    
        if len(text_columns) == 0:
            st.error("No text column available to use as stock names.")
        else:
            index_col = text_columns[0]
    
            chart = (
                alt.Chart(top10)
                .mark_bar(color="red")
                .encode(
                    x=alt.X(index_col, sort=None),
                    y=performance_column
                )
                .properties(width=600, height=400)
            )
    
            st.altair_chart(chart, use_container_width=True)
    
    ## Volume of Green Stock
    
    st.title("Top Average Volume of Green Stock")
    
    @st.cache_data
    def load_data():
        return pd.read_csv("Average_Volume_by_Green_Stock.csv")
    
    df = load_data()
    
    st.subheader("Full Dataset Columns")
    st.write(df.columns.tolist())   # Shows all columns in your CSV
    
    # Find numeric columns automatically
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    st.subheader("Numeric Columns Detected")
    st.write(numeric_columns)
    
    # Dropdown to select performance column
    performance_column = st.selectbox(
        "Select performance column",
        options=df.columns,
        key="performance_column_selectbox_2"
    )
    
    
    # Compute top 10 based on selected column
    top10 = df.sort_values(by=performance_column, ascending=False).head(10)
    
    st.subheader("🏆 Top 10 Performing Average Volume Green Stocks")
    st.dataframe(top10)
    
    # Visual Bar Chart with Green Color
    if len(top10) > 0:
        st.subheader("📊 Performance Chart (Green Bars)")
    
        # find first non-numeric column → usually stock name
        text_columns = df.select_dtypes(exclude=['float64', 'int64']).columns.tolist()
    
        if len(text_columns) == 0:
            st.error("No text column available to use as stock names.")
        else:
            index_col = text_columns[0]
    
            chart = (
                alt.Chart(top10)
                .mark_bar(color="green")
                .encode(
                    x=alt.X(index_col, sort=None),
                    y=performance_column
                )
                .properties(width=600, height=400)
            )
    
            st.altair_chart(chart, use_container_width=True)
    
    
    ## Average Volume of Red Stock
    st.title("Top 10 Average Volume of Red Stock")
    
    @st.cache_data
    def load_data():
        return pd.read_csv("Average_Volume_by_Red_Stock.csv")
    
    df = load_data()
    
    st.subheader("Full Dataset Columns")
    st.write(df.columns.tolist())   # Shows all columns in your CSV
    
    # Find numeric columns automatically
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    st.subheader("Numeric Columns Detected")
    st.write(numeric_columns)
    
    # Dropdown to select performance column
    performance_column = st.selectbox("Select performance column:", numeric_columns)
    
    # Compute top 10 based on selected column
    top10 = df.sort_values(by=performance_column, ascending=False).head(10)
    
    st.subheader("🏆 Top 10 Average Volume of Red Stocks")
    st.dataframe(top10)
    
    # Visual Bar Chart with Green Color
    if len(top10) > 0:
        st.subheader("📊 Performance Chart (Red Bars)")
    
        # find first non-numeric column → usually stock name
        text_columns = df.select_dtypes(exclude=['float64', 'int64']).columns.tolist()
    
        if len(text_columns) == 0:
            st.error("No text column available to use as stock names.")
        else:
            index_col = text_columns[0]
    
            chart = (
                alt.Chart(top10)
                .mark_bar(color="red")
                .encode(
                    x=alt.X(index_col, sort=None),
                    y=performance_column
                )
                .properties(width=600, height=400)
            )
    
            st.altair_chart(chart, use_container_width=True)

## Volatility
elif menu == "Volatility":
    st.title("📉 Stock Volatility Bar Chart")
    
    # Load your uploaded CSV file
    @st.cache_data
    def load_data():
        return pd.read_csv("Volatility.csv")
    
    df = load_data()
    
    st.subheader("Dataset Preview")
    st.dataframe(df)
    
    # Detect column names automatically
    ticker_col = "ticker"   # change if your column name is different
    vol_col = "standard_deviation"  # OR "volatility"
    
    # If both column possibilities exist, choose correct one
    if "standard_deviation" in df.columns:
        vol_col = "standard_deviation"
    elif "volatility" in df.columns:
        vol_col = "volatility"
    
    # Bar Chart
    st.subheader("📊 Volatility Chart (Standard Deviation)")
    fig = px.bar(
        data_frame=df,
        x='Ticker',
        y='Volatility',
    )
    st.plotly_chart(fig, use_container_width=True)

## Cummulative Return
elif menu == "Cummulative":
    st.title("📈 Cumulative Return Dashboard ")
    
    # Load CSV
    @st.cache_data
    def load_data():
        return pd.read_csv("Cumulative_Return.csv")
    
    df = load_data()
    
    st.subheader("Dataset Preview")
    st.dataframe(df)
    
    # Auto-detect column names
    year_col = "year"
    ticker_col = "ticker"
    
    # Detect cumulative return column
    if "cumulative_return" in df.columns:
        cum_col = "cumulative_return"
    elif "cummulative_return" in df.columns:
        cum_col = "cummulative_return"
    else:
        cum_col = df.columns[2]   # third column fallback
    
    # Line chart
    st.subheader("📊 Cumulative Return Line Chart")
    
    fig = px.line(
        data_frame=df,
        x="Year",            # <-- Must match exactly
        y=" Cumulative Return New",  # <-- includes leading space
        color="Ticker"
    )
    st.plotly_chart(fig, use_container_width=True)

## AVERAGE YEARLY RETURN
elif menu == "Average_Yearly":
    st.title("📊 Sector-wise Average Yearly Return")
    
    # Load CSV file
    @st.cache_data
    def load_data():
        return pd.read_csv("Average_Yearly_Return_by_Sector.csv")
    
    df = load_data()
    
    st.subheader("Dataset Preview")
    st.dataframe(df)
    
    # Auto-detect columns
    sector_col = "sector" if "sector" in df.columns else df.columns[0]
    return_col = "average_yearly_return" if "average_yearly_return" in df.columns else df.columns[1]
    
    # Plot bar chart
    st.subheader("📈 Average Yearly Return by Sector")
    
    fig = px.bar(
        df,
        x=sector_col,
        y=return_col,
        title="Average Yearly Return by Sector",
    )
    
    # Optional: make bars green
    fig.update_traces(marker_color="green")
    
    # Display chart
    st.plotly_chart(fig, use_container_width=True)
    
    ## Heatmap Correlation 
elif menu == "Correlated_Heatmap":
    
    st.title("📊 Stock Price Correlation Matrix & Heatmap Dashboard")
    
    # Load CSV
    @st.cache_data
    def load_data():
        return pd.read_csv("correlation_matrix.csv")
    
    df = load_data()
    
    # Keep only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    st.subheader("📈 Correlation Matrix (Table)")
    corr_matrix = numeric_df.corr()
    st.dataframe(corr_matrix)

# Heatmap Chart

    st.subheader("🔥 Correlation Heatmap")
    
    fig = ff.create_annotated_heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns.tolist(),
        y=corr_matrix.columns.tolist(),
        colorscale="Viridis",
        showscale=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

## TOP 5 GAINER MONTHLY RATURN
elif menu == "Monthly_Return":
# -------- PAGE SETTINGS (Responsive) --------
    st.set_page_config(
        page_title="Return Gainer Dashboard",
        layout="wide",          # full-width responsive layout
    )
    
    # -------- TITLE --------
    st.markdown("<h2 style='text-align:center;'>Gain Return Dashboard (Responsive)</h2>", unsafe_allow_html=True)
    
    # -------- LOAD CSV --------
    df = pd.read_csv("Gainer.csv")
    
    df["Month_Year"] = df["Month_Year"].astype(str)
    df["Symbol"] = df["Symbol"].astype(str)
    
    # Sort values for better reading
    df = df.sort_values(["Month_Year", "Percent of MonthlyReturn"], ascending=[True, False])
    
    # -------- RESPONSIVE DATAFRAME --------
    st.subheader("📄 Data Preview")
    st.dataframe(df, use_container_width=True)
    
    # -------- RESPONSIVE COMPACT BAR CHART --------
    st.subheader("📈 Gain Return Chart")
    
    chart = (
        alt.Chart(df)
        .mark_bar(size=10)  # thin bars for compactness
        .encode(
            x=alt.X("Symbol:N", title="Symbol", sort="-y"),
            y=alt.Y("Percent of MonthlyReturn:Q", title="Return (%)"),
            color=alt.Color("Symbol:N", title="Symbol"),
            column=alt.Column(
                "Month_Year:N",
                title="Month",
                header=alt.Header(
                    labelAngle=0,
                    labelFontSize=12
                )
            ),
            tooltip=["Month_Year", "Symbol", "Percent of MonthlyReturn"]
        )
        .properties(
            width=50,   # responsive small width per month
            height= 140  # responsive height
        )
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    ## TOP 5 Looser MONTHLY RETURN

    
    # -------- PAGE SETTINGS (Responsive) --------
    st.set_page_config(
        page_title="Loose Return Dashboard",
        layout="wide",          # full-width responsive layout
    )
    
    # -------- TITLE --------
    st.markdown("<h2 style='text-align:center;'> Loose Return Dashboard (Responsive)</h2>", unsafe_allow_html=True)
    
    # -------- LOAD CSV --------
    df = pd.read_csv("Loose.csv")
    
    df["Month_Year"] = df["Month_Year"].astype(str)
    df["Symbol"] = df["Symbol"].astype(str)
    
    # Sort values for better reading
    df = df.sort_values(["Month_Year", "Percent of MonthlyReturn"], ascending=[True, False])
    
    # -------- RESPONSIVE DATAFRAME --------
    st.subheader("📄 Data Preview")
    st.dataframe(df, use_container_width=True)
    
    # -------- RESPONSIVE COMPACT BAR CHART --------
    st.subheader("Loose Return Chart")
    
    chart = (
        alt.Chart(df)
        .mark_bar(size=10)  # thin bars for compactness
        .encode(
            x=alt.X("Symbol:N", title="Symbol", sort="-y"),
            y=alt.Y("Percent of MonthlyReturn:Q", title="Return (%)"),
            color=alt.Color("Symbol:N", title="Symbol"),
            column=alt.Column(
                "Month_Year:N",
                title="Month",
                header=alt.Header(
                    labelAngle=0,
                    labelFontSize=12
                )
            ),
            tooltip=["Month_Year", "Symbol", "Percent of MonthlyReturn"]
        )
        .properties(
            width=50,   # responsive small width per month
            height= 140  # responsive height
        )
    )

    st.altair_chart(chart, use_container_width=True)
