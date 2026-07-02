# 🎄 Secret Santa App 🎅

Una aplicación web Full-Stack diseñada para automatizar la asignación de Amigos Secretos de forma completamente aleatoria,
enviando los resultados directamente por correo electrónico sin que nadie descubra su asignación antes de tiempo.

## 🚀 Características
- **Algoritmo de Sorteo:** Evita que una persona se auto-asigne o que ocurran bucles cerrados pequeños.
- **Envío Automatizado:** Integración con la API de **SendGrid** para notificaciones por correo electrónico a través de HTTP seguro.
- **Separación de Entornos:** Arquitectura desacoplada lista para desarrollo local o producción.

## 🛠️ Tecnologías Utilizadas

### Frontend
- **React.js** (Vite)
- **Tailwind CSS** (Interfaz responsiva y moderna)
- Desplegado en **Vercel**

### Backend
- **Python 3.11** + **FastAPI**
- **Docker** (Contenerización completa)
- Desplegado en **Render**

## 📂 Estructura del Repositorio
```text
.
├── backend/          # Servidor FastAPI, lógica del sorteo y Dockerfile
└── frontend/         # Interfaz de usuario en React (Vite)
