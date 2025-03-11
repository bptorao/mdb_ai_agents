# 🛠 Instalación de VSCode y Configuración de GitHub Copilot  

Este documento explica cómo instalar **Visual Studio Code (VSCode)** en tu equipo y configurar **GitHub Copilot**, el asistente de inteligencia artificial para desarrollo de código.  

---

## 📥 1. Instalación de Visual Studio Code  

### 🔹 **Descargar VSCode**  
1. Ve al sitio oficial de descarga de VSCode:  
   👉 [https://code.visualstudio.com/](https://code.visualstudio.com/)  
2. Descarga la versión compatible con tu sistema operativo (**Windows, macOS o Linux**).  
3. Ejecuta el instalador y sigue las instrucciones en pantalla.  

### 🔹 **Verificar la instalación**  
Después de instalar, abre una terminal y ejecuta:  

```bash
code --version
```

Si VSCode está instalado correctamente, verás la versión en pantalla.  

---

## 🔌 2. Instalar GitHub Copilot en VSCode  

### **Paso 1: Instalar la Extensión de GitHub Copilot**  
1. Abre VSCode.  
2. Ve a la pestaña de **Extensiones** (`Ctrl + Shift + X` o `Cmd + Shift + X` en macOS).  
3. Busca **GitHub Copilot** y haz clic en **Instalar**.  
4. Espera a que la instalación termine.  

### **Paso 2: Iniciar Sesión en GitHub**  
1. Una vez instalada la extensión, haz clic en **Sign in to GitHub**.  
2. Se abrirá una ventana del navegador. Autoriza el acceso de VSCode a tu cuenta de GitHub.  
3. Si tienes acceso a GitHub Copilot, aparecerá un mensaje de confirmación en VSCode.  

---

## ⚙️ 3. Configurar GitHub Copilot  

Después de instalar la extensión, puedes personalizar el comportamiento de Copilot:  

1. Abre la configuración en VSCode (`Ctrl + ,` o `Cmd + ,` en macOS).  
2. Busca "Copilot" y ajusta las opciones:  
   - **Copilot Suggestions:** Habilita o deshabilita las sugerencias automáticas.  
   - **Copilot Chat:** Activa la función de chat (requiere suscripción).  
   - **Copilot Inline Chat:** Permite recibir sugerencias dentro del código.  

También puedes activar Copilot manualmente dentro de un archivo con:  

```bash
Ctrl + Enter
```

---

## 🚀 4. Probar GitHub Copilot  

1. Crea un nuevo archivo en VSCode (`Ctrl + N`).  
2. Escribe un comentario explicando el código que quieres generar, por ejemplo:  

```python
# Función en Python para calcular el factorial de un número
```

3. **Presiona `Tab` para aceptar la sugerencia** generada por Copilot.  

Si Copilot no responde, asegúrate de que la extensión esté activada y que hayas iniciado sesión en GitHub.  

---

## 🛠 **Solución de Problemas**  

- **No aparecen sugerencias de Copilot:**  
  - Asegúrate de estar **conectado a internet**.  
  - Verifica que Copilot está **activado en la configuración de VSCode**.  
  - Revisa si tu cuenta de GitHub tiene acceso a **Copilot**.  

- **VSCode no detecta la instalación:**  
  - Cierra y vuelve a abrir VSCode.  
  - Si el problema persiste, reinstala la extensión de Copilot.  

---

## ✅ ¡Todo Listo!  

Ahora puedes comenzar a usar **GitHub Copilot** en VSCode para mejorar tu flujo de trabajo y escribir código más rápido 🚀.  
