# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:55:05 2023

@author: EVHARLEY
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Employment Services in BC")

@st.cache_data
def load_data():
    return pd.read_excel("data.xlsx")

if 'data' not in st.session_state:
    st.session_state['data'] = load_data()

st.title("Employment Services in BC")

with st.container(border=True):
    # This creates a group of Metrics which show the current year's value and a delta from the previous year

    st.header('Metrics')

    # Grouping the data by year, and Service Plan Status Code, and getting a count then renaming columns and resetting the index so that
    # the data is able to be managed the correct way in the next steps
    temp1 = st.session_state['data'].groupby([pd.Grouper(freq='1Y', key='SERVICE_START_DATE'), 'SRV_PLAN_STATUS_CD']).agg({
        'SRV_PLAN_STATUS_CD': 'count'
    }).rename(columns={'SRV_PLAN_STATUS_CD': 'count'}).reset_index()

    # Creating a column which holds the previous years value
    temp1['prev'] = temp1['count'].shift(1)
    
    # Doing the same as above, but grouping by Service Status Code
    temp2 = st.session_state['data'].groupby([pd.Grouper(freq='1Y', key='SERVICE_START_DATE'), 'SERVICE_STATUS_CD']).agg({
        'SERVICE_STATUS_CD': 'count'
    }).rename(columns={'SERVICE_STATUS_CD': 'count'}).reset_index()

    temp2['prev'] = temp2['count'].shift(1)

    with st.container():
        st.subheader('Count of Cases by Plan Status Codes')
        col1, col2 = st.columns(2)

        with col1:
            value = temp1.loc[(temp1['SRV_PLAN_STATUS_CD'] == 'Open') & (temp1['SERVICE_START_DATE'].dt.year == 2023), 'count'].reset_index(drop=True)
            prev = temp1.loc[(temp1['SRV_PLAN_STATUS_CD'] == 'Open') & (temp1['SERVICE_START_DATE'].dt.year == 2023), 'prev'].reset_index(drop=True)
            
            st.metric(
                label="Open - 2023",
                value=value[0],
                delta= value[0] - prev[0],
                delta_color='inverse'
            )

        with col2:
            value = temp1.loc[(temp1['SRV_PLAN_STATUS_CD'] == 'Closed') & (temp1['SERVICE_START_DATE'].dt.year == 2023), 'count'].reset_index(drop=True)
            prev = temp1.loc[(temp1['SRV_PLAN_STATUS_CD'] == 'Closed') & (temp1['SERVICE_START_DATE'].dt.year == 2023), 'prev'].reset_index(drop=True)
            
            st.metric(
                label="Closed - 2023",
                value=value[0],
                delta= value[0] - prev[0],
            )

    with st.container():
        st.subheader('Count of Cases by Service Status Codes')
        col3, col4, col5, col6, col7, col8 = st.columns(6)

        with col3:
            value = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'Set Up') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'count'].reset_index(drop=True)
            prev = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'Set Up') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'prev'].reset_index(drop=True)
            
            st.metric(
                label="Set Up - 2023",
                value=value[0],
                delta= value[0] - prev[0],
            )

        with col4:
            value = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'Waiting To Start') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'count'].reset_index(drop=True)
            prev = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'Waiting To Start') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'prev'].reset_index(drop=True)
            
            st.metric(
                label="Waiting to Start - 2023",
                value=value[0],
                delta= value[0] - prev[0],
            )

        with col5:
            value = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'In Progress') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'count'].reset_index(drop=True)
            prev = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'In Progress') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'prev'].reset_index(drop=True)
            
            st.metric(
                label="In Progress - 2023",
                value=value[0],
                delta= value[0] - prev[0],
            )

        with col6:
            value = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'Ended Delivery') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'count'].reset_index(drop=True)
            prev = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'Ended Delivery') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'prev'].reset_index(drop=True)
            
            st.metric(
                label="Ended Delivery - 2023",
                value=value[0],
                delta= value[0] - prev[0],
            )

        with col7:
            value = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'Closed') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'count'].reset_index(drop=True)
            prev = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'Closed') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'prev'].reset_index(drop=True)
            
            st.metric(
                label="Closed - 2023",
                value=value[0],
                delta= value[0] - prev[0],
            )

        with col8:
            value = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'Cancelled') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'count'].reset_index(drop=True)
            prev = temp2.loc[(temp2['SERVICE_STATUS_CD'] == 'Cancelled') & (temp2['SERVICE_START_DATE'].dt.year == 2023), 'prev'].reset_index(drop=True)
            
            st.metric(
                label="Cancelled - 2023",
                value=value[0],
                delta= value[0] - prev[0],
            )

    with st.container():
        temp1 = st.session_state['data'].groupby([pd.Grouper(freq='1Y', key='SERVICE_START_DATE')]).agg({
            'TOTAL_COST_AMT': 'sum',
            'OUTCOME_FEES_PAID_AMT': 'sum',
            'SERVICE_SUPPORT_COST_AMT': 'sum'
            }).reset_index()

        temp1['prev_total_cost'] = temp1['TOTAL_COST_AMT'].shift(1)
        temp1['prev_outcome_fees'] = temp1['OUTCOME_FEES_PAID_AMT'].shift(1)
        temp1['prev_support_cost'] = temp1['SERVICE_SUPPORT_COST_AMT'].shift(1)

        st.subheader("Current Year Costs with Deltas")
        
        col9, col10, col11 = st.columns(3)

        with col9:
            value = temp1.loc[(temp1['SERVICE_START_DATE'].dt.year == 2023), 'TOTAL_COST_AMT'].reset_index(drop=True)
            prev = temp1.loc[(temp1['SERVICE_START_DATE'].dt.year == 2023), 'prev_total_cost'].reset_index(drop=True)

            st.metric(
                label="Total Costs - 2023",
                value='${:,}'.format(value[0]),
                delta= '{:,}'.format(value[0] - prev[0])
            )

        with col10:
            value = temp1.loc[(temp1['SERVICE_START_DATE'].dt.year == 2023), 'OUTCOME_FEES_PAID_AMT'].reset_index(drop=True)
            prev = temp1.loc[(temp1['SERVICE_START_DATE'].dt.year == 2023), 'prev_outcome_fees'].reset_index(drop=True)

            st.metric(
                label="Outcome Fees Paid  - 2023",
                value='${:,}'.format(value[0]),
                delta= '{:,}'.format(value[0] - prev[0])
            )

        with col11:
            value = temp1.loc[(temp1['SERVICE_START_DATE'].dt.year == 2023), 'SERVICE_SUPPORT_COST_AMT'].reset_index(drop=True)
            prev = temp1.loc[(temp1['SERVICE_START_DATE'].dt.year == 2023), 'prev_support_cost'].reset_index(drop=True)

            st.metric(
                label="Service Support Costs - 2023",
                value='${:,}'.format(value[0]),
                delta= '{:,}'.format(value[0] - prev[0])
            )


with st.container(border=True):
    # This section produces a few plots
    st.header("Basic Plots")

    # Grouping the data into monthly bins and by plan name
    temp = st.session_state['data'].groupby([pd.Grouper(freq='1M', key='SERVICE_START_DATE'), 'PLAN_NAME']).agg({
        'TOTAL_COST_AMT': 'sum'
    }).reset_index()
    # Creates a plot of Monthly Total Cost by Plan Name
    fig = px.line(temp, x='SERVICE_START_DATE', y='TOTAL_COST_AMT', color="PLAN_NAME")
    st.plotly_chart(
        figure_or_data=fig
    )

    # As above but gettign a monthly count of cases by gender
    temp = st.session_state['data'].groupby([pd.Grouper(freq='1M', key='SERVICE_START_DATE'), 'GENDER']).agg({
        'GENDER': 'count'
    }).rename(columns={'GENDER': 'count'}).reset_index()
    
    # Plots the Monthl Count of Cases by Gender
    fig = px.line(temp, x='SERVICE_START_DATE', y='count', color="GENDER")
    st.plotly_chart(
        fig
    )
    

with st.container(border=True):
    st.header("Data Tables")

    temp = st.session_state['data'].groupby([pd.Grouper(freq='1Y', key='SERVICE_START_DATE'), 'EDUCATION_LEVEL']).agg({
        'EDUCATION_LEVEL': 'count'
    }).rename(columns={'EDUCATION_LEVEL': 'count'}).reset_index()

    st.subheader('Annual Count of Cases by Education Level')
    st.dataframe(
        pd.pivot_table(temp, values='count', 
                                index='SERVICE_START_DATE', 
                                columns='EDUCATION_LEVEL'),
        column_order=['Elementary', 'Secondary', 'Apprenticeship', 'College', 
                      'University', 'Unknown']
        )
    
    st.subheader('Annual Count of Cases by Service/Subservice')
    temp = st.session_state['data'].groupby([pd.Grouper(freq='1Y', key='SERVICE_START_DATE'), 'SERVICE', 'SUB_SERVICE']).agg({
        'CASE_NUM': 'count'
    }).rename(columns={'CASE_NUM': 'count'}).reset_index()

    st.dataframe(
        pd.pivot_table(
            temp, values='count',
            index=['SERVICE', 'SUB_SERVICE'],
            columns='SERVICE_START_DATE',
        )
    )

    st.subheader('Annual Count of Cases by Client Type')
    temp = st.session_state['data'].groupby([pd.Grouper(freq='1Y', key='SERVICE_START_DATE'), 'CLIENT_TYPE']).agg({
        'CASE_NUM': 'count'
    }).rename(columns={'CASE_NUM': 'count'}).reset_index()

    st.dataframe(
        pd.pivot_table(
            temp, values='count',
            index='CLIENT_TYPE',
            columns='SERVICE_START_DATE',
        )
    )