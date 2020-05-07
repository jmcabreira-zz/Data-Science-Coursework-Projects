import pandas as pd
import streamlit as st
from utils import *
import altair as alt
import matplotlib.pyplot as plt
import webbrowser


def load_data():
    data_path = "data/dashboard_cars.json"
    car_data = pd.read_json(data_path, lines=True)
    clean_data = extra_features(car_data)
    return clean_data

def model_regdate_count(df):
    chart = alt.Chart(df, width = 600).mark_bar().encode(
    x = 'count()',
    y = alt.Y('model', sort = alt.Sort(encoding = 'x', order= 'descending')),
    tooltip = ['regdate','count()'],
    color = 'regdate:O'
    ).interactive()
    return chart

def financial_regdate(df):
    chart = alt.Chart(df, width=600).mark_bar().encode(
    x = 'count()',
    y = alt.Y('financial', sort = alt.Sort(encoding = 'x', order= 'descending')),
    tooltip = ['regdate','count()'],
    color = 'regdate:O'
    ).interactive()
    return chart

def model_power_count(df):
    chart = alt.Chart(df, width = 600).mark_bar().encode(
    x = 'count()',
    y = alt.Y('model', sort = alt.Sort(encoding = 'x', order= 'descending')),
    tooltip = ['motorpower','count()'],
    color = 'motorpower:O'
    ).interactive()
    return chart

def main():
    st.image("images/CabreiraLogo.png")
    st.write("# Car Recommendation System Dashboard")


    options = ['Project Motivation', 'Dashboard','Contact me']
    choice = st.sidebar.selectbox("Options", options)

    if choice =='Project Motivation':
        st.markdown(proj_mot)
        st.subheader('Application Diagram')
        st.image("images/Diagram.png")


    elif choice == 'Dashboard':
        st.sidebar.header("Dashboard")
        st.subheader('Cars information')
        st.info(" This dashboard shows information regarding cars with the highest scores")
        data = load_data()
        if st.checkbox('Show Data'):
            st.dataframe(data.head())
            if st.checkbox('Show Shape'):
                st.write(data.shape)
            if st.checkbox('Show Columns'):
                columns = data.columns.to_list()
                st.write(columns)
            if st.checkbox('Show Statistics'):
                st.write(data.describe().T)
            if st.checkbox('Show Car Classes'):
                st.write(data['brand'].value_counts())

        st.header('Bar Charts')
        st.subheader('Model - Regdate')
        chart1 = model_regdate_count(data)
        chart1
        st.subheader('Financial Status - Regdate')
        chart2 = financial_regdate(data)
        chart2
        st.subheader('Model - Motor power')
        chart3 = model_power_count(data)
        chart3


    elif choice == 'Contact me':
        st.sidebar.header("Jonathan Cabreira")

        url1 = 'https://www.linkedin.com/in/jonathan-cabreira-4635aa103/'
        url2 = 'https://medium.com/@cabreirajm'
        url3 = 'https://github.com/jmcabreira'
        if st.sidebar.button('Linkedin'):
            webbrowser.open_new_tab(url1)
        if st.sidebar.button('Medium'):
            webbrowser.open_new_tab(url2)
        if st.sidebar.button('GitHub'):
            webbrowser.open_new_tab(url3)

proj_mot = """ After a year living on the Emerald Isle – Ireland – it is time to move back to Brazil.

It is very difficult to live in Rio de Janeiro, Brazil without a car and I am now in the market to buy a new one. As you probably know, I am a data-driven person, and based on that I decided to approach this problem as a good Data Scientist.

I built a car recommendation system. The web app searches for cars on a webpage processes the data and passes it through a machine learning model in order to list and display cars that are more related to what I am looking for."""

if __name__ == '__main__':
    main()
