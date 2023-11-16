import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import altair as alt

data = pd.read_pickle("data/dataframe.pkl")
#vie = vie.set_index("date")
#md = pd.read_pickle("data/moedling.pkl")
#md = md.set_index("date")

st.markdown("# :flag-be: Bart's :penguin: data :rainbow[project]!")

st.markdown("### A short :blue[summary:]")
st.markdown("""This project automatically downloads air quality, :thermometer: and humidty data from Vienna and Mödling.\
            This data is then converted into 2 csv files with automated Bash/awk scripts,
            cleaned up a little more with Python and uploaded to this Streamlit app.""")

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
#start_date = min_date #remove later
end_date = start_date + timedelta(days=1)


#moed_temp = md.loc[start_date:end_date][[option]]
#wien_temp = vie.loc[start_date:end_date][[option]]

#moed_temp["moedling"] = moed_temp[option]
#wien_temp["wien"] = wien_temp[option]

# chart1 = alt.Chart(moed_temp.reset_index()).mark_line().encode(
#     x= alt.X("date:T", title="date"),
#     y= alt.Y("moedling", title=option),
#     color=alt.value("blue"),
# )

# chart2 = alt.Chart(wien_temp.reset_index()).mark_line().encode(
#     x= alt.X("date:T", title="date"),
#     y= alt.Y("wien", title=option),
#     color=alt.value("red"),
#     text = alt.Text(alt.value("Wien"))
# )

# chart1 + chart2

data_temp = data[option].unstack(level=0)
data_temp = data_temp.loc[start_date:end_date]

st.subheader(f"{option.title()}: Mödling <-> Wien")
st.line_chart(data_temp, y=["moedling", "vienna"])
# st.subheader("Vienna")
# st.line_chart(wien_temp, y=[option, option2])





