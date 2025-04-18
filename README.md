# 📚 StudyMade – Django Based Collaborative Educational Platform

StudyMade is a Django-based web application designed to help students to collaborate and information categorized by each topics and concepts. The goal is to make learning more organized for students in a simple, user-friendly interface.

---

## ✨ Features

- 🔐 **User Authentication**: Login and Registration system for secure access.
- 🗂️ **Room & Topic Selection**: Users can select their topic and create room to collaborate with other students.
- 🔍 **Simple UI**: Clean, responsive interface using HTML, CSS, and Bootstrap.


---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JS
- **Backend**: Python, Django
- **Database**: SQLite (default Django DB)

---
## 🚀 How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Vignesh21J/Django-StudyMade-Website-Project.git
   cd Django-StudyMade-Website-Project

2. **Create Virtual Environment**
  python -m venv env
  env\Scripts\activate   # On Windows

3. **Install Dependencies**
   pip install -r requirements.txt
   
4. **Run Migrations**
  python manage.py makemigrations
  python manage.py migrate

5. **Create Superuser**
  python manage.py createsuperuser

6. **Run the Development Server**
  python manage.py runserver

7. Open your browser and visit: http://127.0.0.1:8000/
  
