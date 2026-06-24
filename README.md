# Secret Santa 🎁

¡Bienvenido al Generador de Secret Santa! Esta es una aplicación web interactiva desarrollada con **Streamlit** y **Python** que automatiza por completo el sorteo de tu amigo secreto. 

A diferencia de las versiones tradicionales por terminal, esta aplicación se ejecuta directamente desde el navegador web, elimina la necesidad de gestionar archivos CSV manuales y envía los resultados de forma instantánea y confidencial a través del correo electrónico de cada participante.

---

## 🚀 Características principales

* **Interfaz Web Intuitiva:** Añade participantes (Nombre y Correo) uno a uno mediante un formulario dinámico en pantalla.
* **Sorteo Inteligente:** Algoritmo aleatorio que garantiza que nadie se asigne a sí mismo.
* **Memoria de Sesión Dinámica:** Gestión de la lista en tiempo real usando `st.session_state` (sin almacenar datos sensibles de forma permanente).
* **Envío Masivo Optimizado:** Conexión única y segura vía SMTP con Gmail que dispara todos los correos en un par de segundos.
* **Seguridad Primero:** Integración nativa con sistemas de variables de entorno para proteger las credenciales de correo electrónico.

---

## 📦 Instalación

Clona el repositorio y crea un entorno virtual:

```bash
git clone https://github.com/tu_usuario/secret_santa.git
cd secret_santa
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows
pip install -e .
