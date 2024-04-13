import streamlit as st
import pandas as pd
import plotly.express as px
from workflow.manip import *
import os 
import warnings
warnings.filterwarnings('ignore')


# Titre de la page via le web
st.set_page_config(page_title = "Dashboad imo France", page_icon = ":bar_chart:", layout = "wide")

st.subheader(" :bar_chart: Tendance de l'immobilier en France ")

tab1, tab2 = st.tabs(["Cat", "Dog"])

# 
#add_selecbox = st.sidebar.selectbox("Slectionnez", df_fimo.code_departement.unique)

st.sidebar.header("Choisir le filtre : ")
depart = st.sidebar.multiselect(
    "Selectionner le département",
    options = df_fimo["code_departement"].unique()
)

typ_log = st.sidebar.multiselect(
    "Selectionner le type de local",
    options = df_fimo["type_local"].unique()
)



with tab1:
    input_text = st.text_area(label = "entrez votre input")
    st.write(input_text)
    st.dataframe(df_fimo)


with tab2:
    input_v = st.text_area(label = "entrez votre code")
    st.write(input_v)
    st.dataframe(df_data)
