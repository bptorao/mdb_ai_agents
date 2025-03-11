# 🚀 Introducción a Streamlit  

## 📌 ¿Qué es Streamlit?  
**Streamlit** es un framework de Python que permite desarrollar **aplicaciones web interactivas** de forma rápida y sencilla, sin necesidad de conocimientos avanzados de desarrollo frontend.  

Es ideal para crear dashboards, visualizar datos y construir interfaces para modelos de machine learning con pocas líneas de código.  

📌 **Sitio web oficial:** [https://streamlit.io/](https://streamlit.io/)  

---

## 🛠 Instalación de Streamlit  

Para instalar Streamlit en tu entorno de Python, usa el siguiente comando:  

```bash
pip install streamlit
```

Verifica que la instalación fue correcta ejecutando:  

```bash
streamlit hello
```

Si la instalación fue exitosa, se abrirá un demo interactivo en tu navegador.  

---

## 🏗️ Creando una Aplicación Básica  

Para empezar, crea un nuevo archivo **`app.py`** y añade el siguiente código:  

```python
import streamlit as st

st.title("Mi Primera App en Streamlit 🚀")
st.write("¡Hola! Esta es una aplicación web creada con Streamlit.")
```

Ejecuta la aplicación con:  

```bash
streamlit run app.py
```

Esto abrirá la app en tu navegador en `http://localhost:8501/`.  

---

## 📊 Ejemplos Sencillos  

### **1️⃣ Input y Salida de Datos**
```python
import streamlit as st

nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.write(f"¡Hola, {nombre}! 🎉")
```

### **2️⃣ Gráficos con Matplotlib**
```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)
```

### **3️⃣ Carga de Datos y Visualización**
```python
import streamlit as st
import pandas as pd

st.title("Carga y Visualización de Datos")

archivo = st.file_uploader("Sube un archivo CSV", type=["csv"])
if archivo is not None:
    df = pd.read_csv(archivo)
    st.write(df.head())
```

---

## 🎯 ¿Por Qué Usar Streamlit?  
✔ **Fácil de aprender y usar** – Solo necesitas Python.  
✔ **Interfaz web sin conocimientos de frontend** – No requiere HTML, CSS o JS.  
✔ **Ideal para visualizar datos** – Compatible con Pandas, Matplotlib, Plotly, etc.  
✔ **Rápido despliegue** – Se puede compartir con un solo comando.  

Para más información, revisa la documentación oficial:  
🔗 [https://docs.streamlit.io/](https://docs.streamlit.io/)  
