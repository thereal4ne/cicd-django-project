# CI/CD Pipeline for a Django Application 🚀

This project demonstrates a complete **CI/CD pipeline** for a Django web application using:

- Git & GitHub
- GitHub Actions (Continuous Integration)
- Render (Continuous Deployment)
- Gunicorn (Production server)

---

## 🌐 Live Application

https://cicd-django-project.onrender.com

---

## 🧠 What this project shows

This project is not just a Django app.  
It shows how modern companies automatically test and deploy code.

Whenever code is pushed to GitHub:

1. GitHub Actions automatically runs tests (CI)
2. If tests pass, Render automatically deploys the app (CD)
3. The live website updates without manual work

---

## ⚙️ CI/CD Flow

Edit Code → git commit → git push
↓
GitHub Actions runs Django tests
↓
Render deploys the latest version
↓
Live site updates


---

## 🧪 Continuous Integration (CI)

GitHub Actions is configured to:

- Install dependencies from `requirements.txt`
- Run Django tests using `python manage.py test`
- Fail the pipeline if tests fail

File used: `.github/workflows/ci.yml`

---

## 🚀 Continuous Deployment (CD)

Render is connected to the GitHub repository.

When CI passes and code is pushed:
- Render pulls latest code
- Installs dependencies
- Runs the app using Gunicorn
- Deploys the updated site

---

## 🔐 Environment Variables

Sensitive settings are not stored in code. They are stored in Render:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`

This follows real production best practices.

---

## 📦 Requirements

All dependencies are listed in `requirements.txt`, including:

- Django
- Gunicorn

---

## 🏁 How to run locally

```bash
pip install -r requirements.txt
python manage.py runserver
```
---

## ✅ Outcome

This project demonstrates a real-world CI/CD setup for a Django application that is:

- Automatically tested
- Automatically deployed
- Production-ready


