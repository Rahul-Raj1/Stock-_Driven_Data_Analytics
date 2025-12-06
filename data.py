import streamlit as st
import pandas as pd

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


