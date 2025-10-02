# 🧠 Quiz.AI – Sistema de Cuestionarios Inteligentes

![Quiz.AI Banner](https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django) 
![React](https://img.shields.io/badge/React-19-blue?style=for-the-badge&logo=react)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

📚 **Quiz.AI** es una aplicación fullstack desarrollada con **Django REST Framework (backend)** y **React + Bootstrap (frontend)** para la gestión y resolución de cuestionarios interactivos.  
Permite listar quizzes, contestar preguntas, enviar respuestas y obtener calificación automática con retroalimentación.

---

## 🚀 Funcionalidades principales

✅ Listado de quizzes con imagen y descripción.  
✅ Detalle de cada quiz con preguntas y opciones.  
✅ Selección de alternativas y envío de respuestas.  
✅ Calificación automática con nota, porcentaje y feedback (emoji + mensaje).  
✅ API REST para CRUD de quizzes, preguntas y opciones.  
✅ Interfaz moderna con React + Bootstrap.  

---

## 📂 Estructura del proyecto

quizz-AI-mejorado-/
│── backend/ # Django + DRF (API REST)
│ ├── config/
│ ├── quizzes/
│ └── db.sqlite3
│
│── frontend/ # React + Bootstrap
│ ├── src/components/
│ │ ├── QuizList.jsx
│ │ └── QuizDetail.jsx
│ └── package.json
│
└── README.md

yaml
Copiar código

---

## ⚙️ Instalación

### 🔹 1. Backend (Django REST Framework)
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
El backend correrá en 👉 http://127.0.0.1:8000/api/v1/

🔹 2. Frontend (React + Bootstrap)
bash
Copiar código
cd frontend
npm install
npm start
El frontend correrá en 👉 http://localhost:3000/

🔗 Endpoints principales (API REST)
📌 API Root
bash
Copiar código
GET /api/v1/
📌 Quizzes
bash
Copiar código
GET    /api/v1/quizzes/        # Lista de quizzes
GET    /api/v1/quizzes/{id}/   # Detalle de un quiz
POST   /api/v1/quizzes/        # Crear quiz
POST   /api/v1/quizzes/{id}/submit/   # Enviar respuestas y calcular nota
📌 Preguntas
bash
Copiar código
GET    /api/v1/questions/
POST   /api/v1/questions/
📌 Opciones
bash
Copiar código
GET    /api/v1/choices/
POST   /api/v1/choices/
🎮 Flujo de uso
Entra al frontend y verás la lista de quizzes con su imagen.

Haz clic en 🚀 Empezar para acceder al quiz.

Selecciona tus respuestas en cada pregunta.

Presiona 📤 Enviar respuestas.

El sistema muestra tu nota, porcentaje y retroalimentación (ejemplo: 🏆 A – sobresaliente).📝 Licencia

Este proyecto está bajo la licencia MIT – libre para modificar y usar con fines educativos.

🚀 Desarrollado por Hazielcode
