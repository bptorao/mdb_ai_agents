# 📌 Instrucciones para Acceder y Subir tu Solución al Repositorio `mdb_ai_agents`

Este documento explica cómo solicitar acceso al repositorio, clonarlo en tu equipo, añadir tu solución y configurar GitHub con autenticación SSH para hacer `push` de tu implementación.

---

## 🚀 1. Solicitar Acceso al Repositorio  

Para obtener acceso al repositorio privado **`mdb_ai_agents`**, sigue estos pasos:  

1. Envíame un correo con tu dirección de GitHub a: **bueka.torao@gmail.com**.  
2. Te enviaré una invitación para acceder al repositorio en GitHub.
[mdb_ai_agents](https://github.com/bptorao/mdb_ai_agents)
3. Una vez recibida la invitación, acéptala desde [GitHub → Invites](https://github.com/settings/organizations).  

---

## 🛠 2. Clonar el Repositorio en tu Equipo  

Después de aceptar la invitación, puedes clonar el repositorio en tu máquina local ejecutando el siguiente comando en tu terminal:  

```bash
git clone git@github.com:bptorao/mdb_ai_agents.git
```

Si prefieres clonar usando HTTPS, puedes hacerlo con:  

```bash
git clone https://github.com/[TU_USUARIO]/mdb_ai_agents.git
```

Luego, entra en la carpeta del repositorio:  

```bash
cd mdb_ai_agents
```

---

## 📁 3. Crear y Actualizar tu Carpeta de Solución  

Cada equipo o persona debe crear su propia carpeta dentro de `solutions`, siguiendo estos pasos:  

1. Copia la carpeta `template_group_name` dentro de `solutions` y renómbrala con tu nombre de equipo o usuario:  

```bash
cp -r solutions/template_group_name solutions/tu_nombre_equipo
```

2. Entra en la carpeta y edita el `README.md` para incluir la información de tu agente:  

```bash
cd solutions/tu_nombre_equipo
nano README.md
```

📌 **Información mínima en el README:**  
- Nombre del equipo o integrante(s).  
- Descripción del agente de AI implementado.  
- Cómo ejecutarlo.  

---

## 🔑 4. Configurar Claves SSH para Hacer `Push` a GitHub  

Si aún no has configurado una clave SSH en tu cuenta de GitHub, sigue estos pasos:  

### 🔹 Generar una nueva clave SSH (si no tienes una)  

Ejecuta el siguiente comando en la terminal:  

```bash
ssh-keygen -t ed25519 -C "tu_correo@ejemplo.com"
```

Presiona `Enter` para aceptar la ubicación predeterminada y luego establece una contraseña opcional.  

Ahora, añade la clave SSH al agente de autenticación:  

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### 🔹 Agregar la clave SSH a GitHub  

1. Copia tu clave pública con:  

```bash
cat ~/.ssh/id_ed25519.pub
```

2. Ve a **GitHub → Settings → SSH and GPG keys** o usa este enlace: [Configurar SSH en GitHub](https://github.com/settings/keys).  
3. Haz clic en **"New SSH Key"**, pon un nombre y pega tu clave pública.  
4. Guarda los cambios.  

Para verificar que la conexión funciona correctamente:  

```bash
ssh -T git@github.com
```

Si ves un mensaje como `"Hi [TU_USUARIO]! You've successfully authenticated"`, la configuración fue exitosa.  

---

## 📤 5. Subir tu Solución al Repositorio  

Después de implementar tu agente, sube tu código siguiendo estos pasos:  

1. Asegúrate de estar en la rama `main`:  

```bash
git checkout main
```

2. Añade los cambios al repositorio:  

```bash
git add solutions/tu_nombre_equipo
git commit -m "[nombre equipo] descripcion del cambio"
git push origin main
```

Si usas HTTPS y GitHub te pide autenticación en cada `push`, considera usar [GitHub CLI](https://cli.github.com/) o configurar un **token de acceso personal**.  

---

## ✅ ¡Todo Listo!  

Ahora tu solución está en el repositorio. Si necesitas actualizarla, simplemente haz cambios en tu carpeta y repite el proceso de `git add`, `commit` y `push`.  

Si tienes dudas, revisa la documentación oficial de GitHub o contacta conmigo. 🚀  

