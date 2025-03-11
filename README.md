#  **AI Agents Workshop - Master Big Data - Esesa 2025**  

Este repositorio contiene los recursos necesarios para el desarrollo de agentes de inteligencia artificial en el ejercicio práctico del workshop.  

 **Objetivo:**  
Los participantes desarrollarán su propio **agente de AI** en **130 minutos**, utilizando herramientas como la **API de OpenAI**, una **interfaz en Streamlit**, y una **base de datos con ventas de un videoclub** (opcional).  

---

##  **Estructura del Repositorio**  

 **notebooks/** *(Carpeta con Jupyter Notebooks de referencia)*  
-  `01_Testing_Ollama_API.ipynb`  Explicación y prueba de la API de **Ollama** en local.  
-  `01_Testing_OpenAI_API.ipynb`  Uso de la **API de OpenAI** para interactuar con modelos LLM.  
-  `01_Connecting_Videoclub_DB.ipynb`  Cómo conectarse a la **base de datos del videoclub** y realizar consultas.  

 **app/** *(Ejemplo de implementación en Streamlit)*  
-  `copilot_app.py`  Aplicación en **Streamlit** que implementa un **Copilot Agent**.  
-  `run_copilot_app.sh`  Script para ejecutar el **Copilot Agent** en local.  

 **database/** *(Recursos de la base de datos del videoclub)*  
-  `er_diagram.png`  **Diagrama Entidad-Relación (ER)** de la base de datos del videoclub.  

 **requirements/** *(Dependencias del proyecto)*  
-  `requirements.txt`  Lista de paquetes necesarios para ejecutar los ejemplos y el agente en **Streamlit**.  

 **docs/** *(Guías y documentación del repositorio)*  
-  `instrucciones_GITHUB.md`  Explica cómo acceder al repositorio, configurar SSH y subir soluciones.  

 **solutions/** *(Carpeta donde cada equipo subirá su solución personalizada)*  
-  **Cada equipo debe copiar la plantilla `template_group_name` y renombrarla con su nombre**.  
-  **Explicación detallada en `instrucciones_GITHUB.md`**.  

---

##  **Cómo Empezar**  

1 **Solicitar acceso al repositorio:**  
   - Envía tu correo de GitHub para recibir una invitación.  

2 **Clonar el repositorio:**  
   ```bash
   git clone git@github.com:TUTORIAL/mdb_ai_agents.git
   cd mdb_ai_agents
   ```

3 **Configurar el entorno:**  
   - Instala las dependencias ejecutando:  
   ```bash
   pip install -r requirements.txt
   ```

4 **Ejecutar un ejemplo en Streamlit:**  
   ```bash
   bash run_copilot_app.sh
   ```

5 **Leer los notebooks para entender cómo interactuar con las APIs y la base de datos.**  

---

##  **Desarrollo del Agente de AI**  

 **Los equipos deben crear un agente de AI siguiendo los pasos indicados en la masterclass.**  
 Cada solución debe estar dentro de `solutions/tu_nombre_equipo/` con un `README.md` explicando la implementación.  

 **Objetivo:** Construir un agente funcional en 90 minutos.  

 Para más detalles, consulta **`instrucciones_GITHUB.md`**.  

---

##  **Contribuciones y Preguntas**  

Si tienes dudas o problemas, revisa la documentación o pregunta en el foro del workshop. ¡Buena suerte desarrollando tu agente!  