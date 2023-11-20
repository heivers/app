import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os
from os.path import abspath, dirname 
import altair as alt

os.chdir(dirname(abspath(__file__)))

translate = {'ozone': 'ozon', 'sulfur dioxide': 'schwefeldioxid', 'air temperature': 'lufttemperatur'
             , 'wind speed': 'windgeschwindigkeit', 'humidity': 'luftfeuchtigkeit', 'nitrogen dioxide': 'stickstoffdioxid', 
             'nitrogen oxides': 'stickoxide', 'particulate matter': 'feinstaub', 'carbon monoxide': 'kohlenmonoxid'}

unit = {("lufttemperatur",) : "°C", "windgeschwindigkeit": "km/h", 
        ("ozon", "schwefeldioxid", "stickstoffdioxid","stickoxide", "feinstaub"): "µg/m³",
        ("kohlenmonoxid",): "mg/m³", ("luftfeuchtigkeit",): "%"}

data = pd.read_pickle("data/dataframe.pkl")

st.markdown("# Bart's :penguin: data :rainbow[assignment]!")


st.markdown("### A short :blue[summary:]")
st.markdown(":blue[Mödling] (my home) is just outside of :red[Vienna]. Does it have better air-quality?")
st.markdown("The assignment consists of:")
st.markdown("* Bash scripts to download air quality, :thermometer: and humidty data (curl)")
st.markdown("* Bash and awk scripts to format into an easy to read csv-file for Pandas")
st.markdown("* Python script to deal with N/A values and resample the data")
st.markdown("* The Streamlit app :balloon:")


with st.sidebar:

    st.subheader("Select a start date:")

    min_date = datetime(2023, 11, 12)
    today = datetime.now()
    max_date = datetime.date(today) - timedelta(days=1)

    start_date = st.date_input("Pick a start date: ", min_value=min_date, max_value=max_date, value=max_date)

    st.subheader("Select an end date:")

    end_date = st.date_input("Pick an end date: ", min_value=min_date, max_value=max_date, value=max_date, key=42)

    if start_date > end_date:
        st.markdown("## :red[Start date cannot come after End Date!]")

    st.subheader("Select :")

    option = st.selectbox(
    "Select the item you wish to view",
    translate.keys()
    )

val = option
option = translate[val]
for k in unit:
    if option in k:
        m_unit = unit[k]
        break


end_date = end_date + timedelta(days=1)

data_temp = data[option].unstack(level=0)
data_temp = data_temp.loc[start_date:end_date]
data_temp = data_temp[:-1]

st.subheader(f"{val.title()} {m_unit}: Mödling <-> Vienna")
st.line_chart(data_temp, y=["moedling", "vienna"], color=["#00008B", "#FF0000"])

st.divider()

st.caption(f"Actual data for {val.title()} in {m_unit}")
st.dataframe(data_temp)

st.divider()

st.text("Please note that the analytics was not the main part of this assignment.")
st.text("Missing values were handled by simple backfilling.")
st.write("Data retrieved from [Opendata Austria](https://www.data.gv.at)")
