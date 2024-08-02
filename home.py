import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    all_dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    all_temperatures = [10, 11, 15]
    all_temperatures = [days * i for i in all_temperatures]
    return all_dates, all_temperatures


dates, temperatures = get_data(days)

figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperatures (C)"})
st.plotly_chart(figure)
