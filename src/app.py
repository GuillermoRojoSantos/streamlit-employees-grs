import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

st.title("Empleatronix-GRS")
st.text("Todos los datos sobre los empleados en una aplicación")

df = pd.read_csv("employees.csv")
st.write(df)

st.divider()

#Creamos las columnas para guardar los componentes que editen el plot
col1, col2, col3 = st.columns(3)
with col1:
    color = st.color_picker("Elige color para las barras", "#3475B3")
with col2:
    #Con value=True le decimso al toggle que se cargue activado
    s_name = st.toggle("Mostrar el Nombre",value=True)
with col3:
    s_salary = st.toggle("Mostrar el Sueldo en la barra")

#Creamos el plot
fig, ax = plt.subplots(figsize=(8,5))
ax.set_xlim(0, 4500)
bars = ax.barh(df["full name"],df.salary,color=color)
if s_salary:
    #Si el toggle de salario está activado, mostramos el salario de los trabajadores al final de las barras
   ax.bar_label(bars,fmt="%d€",padding=5)
if not s_name:
    #Si el toggle de nombre está desactivado, borramos los nombres
    ax.set_yticks([])

st.pyplot(fig)

st.write("© Guillermo Rojo Santos - CPIFP Alan Turing")