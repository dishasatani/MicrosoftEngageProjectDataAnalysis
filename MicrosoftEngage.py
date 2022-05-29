import numpy as np
import pandas as pd
from IPython.core.display import HTML
from matplotlib import pyplot as plt
from IPython.display import display
import streamlit as st
from PIL import Image

st.title("Microsoft Engage Data Analysis Project")
image = Image.open('signup.png')


st.image(image, caption='MS-Engage 2022')
plt.rcParams.update({'font.size': 26})


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 2)


df = pd.read_csv('cars_engage_2022.csv')



option=st.selectbox("Enter your choice",("show csv file",
"show all car frequency with make name",
"show all car frequency with make and model",
"display the details of particular car:",
"Types of car in terms of price:",
"Avarage price comparison"))

if 'show csv file' in option: 
    st.write(df)

if 'show all car frequency with make name' in option: 
    count=df.groupby(["Make"]).size()
    st.write(count)

if 'show all car frequency with make and model' in option:
    counts=df.groupby(["Make", "Model"]).size()
    st.write(counts)
    

if 'display the details of particular car:' in option: 
    
    st.write(pd.Series(df["Make"].unique()))
    st.write("enter the car's make from above list")
    cmake = st.text_input('cmake','Tata')
    st.write(pd.Series((df.loc[ df["Make"] == cmake]["Model"]).unique()))
    st.write("enter the car's model from above list: ")
    cmodel = st.text_input('cmodel','Bolt')
    st.write(pd.Series((df.loc[ (df["Make"] == cmake)&(df["Model"] == cmodel)]["Variant"]).unique()))
    st.write("enter the car's variant from above list: ")
    cvariant = st.text_input('cvariant','Xm Petrol')
    st.write(df.loc[(df['Make'] == cmake)&(df['Model'] == cmodel)&(df['Variant'] == cvariant)])
    

if 'Types of car in terms of price:' in option: 
    st.write(pd.Series(df["Make"].unique()))
    st.write("enter the car's make from above list")
    cmake = st.text_input('cmake','Tata')

    options=st.selectbox("Enter your choice",("Entry Level",
    "Middle level",
    "luxurious"))

    if 'Entry Level' in options:
        df['Ex-Showroom_Price1'] = df['Ex-Showroom_Price'].str.replace(',','',regex=True).str.replace('Rs.','',regex=True).astype('int')            
        st.write(df.loc[ (df["Make"] == cmake ) & ( (df["Ex-Showroom_Price1"]>=200000)&(df["Ex-Showroom_Price1"]<700000)) ])
    
    if 'Middle level' in options:
        df['Ex-Showroom_Price1'] = df['Ex-Showroom_Price'].str.replace(',','',regex=True).str.replace('Rs.','',regex=True).astype('int')
        st.write(df.loc[ (df["Make"] == cmake ) & ( (df["Ex-Showroom_Price1"]>=700000)&(df["Ex-Showroom_Price1"]<2000000)) ])
        
    if 'luxurious' in options:
        df['Ex-Showroom_Price1'] = df['Ex-Showroom_Price'].str.replace(',','',regex=True).str.replace('Rs.','',regex=True).astype('int')
        st.write(df.loc[ (df["Make"] == cmake ) & (df["Ex-Showroom_Price1"]>=2000000) ])
        




if 'Avarage price comparison' in option: 
    ops=st.selectbox("Enter your choice",("Entry Level",
    "Middle level",
    "luxurious"))

    if 'Entry Level' in ops:
        df1 = df.astype(str, errors='ignore')
        a=[]
        a=np.array(df1["Make"].unique())
        f=[]
        df1['Ex-Showroom_Price1'] = df1['Ex-Showroom_Price'].str.replace(',','',regex=True).str.replace('Rs.','',regex=True).astype('int')
        for i in range(len(a)):
            p_avg=df1.loc[ (df1["Make"] == a[i] ) & ( (df1["Ex-Showroom_Price1"]>=200000)&(df1["Ex-Showroom_Price1"]<700000)) ]['Ex-Showroom_Price1']
            f.append(p_avg.mean())
            b = np.where(np.isnan(f), 0, f)

        chart_data = pd.DataFrame(b,a)
        st.bar_chart(chart_data)
        
    if 'Middle level' in ops:
        df1 = df.astype(str, errors='ignore')
        a=[]
        a=np.array(df1["Make"].unique())
        f=[]
        df1['Ex-Showroom_Price1'] = df1['Ex-Showroom_Price'].str.replace(',','',regex=True).str.replace('Rs.','',regex=True).astype('int')
        for i in range(len(a)):
            p_avg=df1.loc[ (df1["Make"] == a[i] ) & ( (df1["Ex-Showroom_Price1"]>=700000)&(df1["Ex-Showroom_Price1"]<2000000)) ]['Ex-Showroom_Price1']
            f.append(p_avg.mean())
            b = np.where(np.isnan(f), 0, f)

        chart_data = pd.DataFrame(b,a)
        st.bar_chart(chart_data)
        
    if 'luxurious' in ops:
        df1 = df.astype(str, errors='ignore')
        a=[]
        a=np.array(df1["Make"].unique())
        f=[]
        df1['Ex-Showroom_Price1'] = df1['Ex-Showroom_Price'].str.replace(',','',regex=True).str.replace('Rs.','',regex=True).astype('int')
        for i in range(len(a)):
            p_avg=df1.loc[ (df1["Make"] == a[i] ) & (df1["Ex-Showroom_Price1"]>=2000000)]['Ex-Showroom_Price1']
            f.append(p_avg.mean())
            b = np.where(np.isnan(f), 0, f)

        chart_data = pd.DataFrame(b,a)
        st.bar_chart(chart_data)
        



