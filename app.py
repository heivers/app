import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import altair as alt

data = pd.read_pickle("data/dataframe.pkl")

st.markdown("# Bart's :penguin: data :rainbow[assignment]!")

st.markdown("### A short :blue[summary:]")
st.markdown("""This project (my not exactely :strawberry: Pi) automatically downloads air quality, :thermometer: and humidty data from Vienna and Mödling.\
            This data is then converted into 2 csv files with automated Bash/awk scripts,
            cleaned up a little more with Python and uploaded to this Streamlit app.
            Mödling (my home) is just outside of Vienna. Does it have better air-quality?""")

with st.sidebar:

    st.subheader("Select a date:")

    min_date = datetime(2023, 11, 12)
    today = datetime.now()
    max_date = datetime.date(today) - timedelta(days=1)

    start_date = st.date_input("Pick a date: ", min_value=min_date, max_value=max_date, value=max_date)
      

    st.subheader("Select :")

    option = st.selectbox(
    "Select the item you wish to view",
    data.columns
    )

end_date = start_date + timedelta(days=1)

data_temp = data[option].unstack(level=0)
data_temp = data_temp.loc[start_date:end_date]
data_temp = data_temp[:-1]

st.subheader(f"{option.title()}: Mödling <-> Wien")
st.line_chart(data_temp, y=["moedling", "vienna"])

st.divider()

st.caption(f"The actual data for {option.title()}")
st.dataframe(data_temp)

st.divider()

st.text("Please note that the analytics was not the main part of this assignment.")
st.text("Some values were missing and were backfilled.")
