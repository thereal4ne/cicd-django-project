CI/CD Pipeline for a Django Task Manager 🚀

This project demonstrates a complete CI/CD pipeline for a Django web application deployed to the cloud.

It is not just a Django app — it shows how modern software is automatically tested and deployed using industry DevOps practices.

🌐 Live Application

https://cicd-django-project.onrender.com

🧠 What this project demonstrates

This project shows how professional teams ensure:

Code is automatically tested before deployment

Broken code never reaches production

Deployment happens automatically without manual steps

A database-driven Django app runs in production

Whenever code is pushed to GitHub:

GitHub Actions runs automated tests (Continuous Integration)

If tests pass, Render automatically deploys the app (Continuous Deployment)

The live website updates automatically

🧩 Features of the Web Application

This is a Task Manager built using Django:

Add new tasks

Mark tasks as completed

Delete tasks

Bootstrap-based responsive UI

SQLite database integration

⚙️ CI/CD Workflow
Edit Code → git commit → git push
        ↓
GitHub Actions runs Django tests
        ↓
If tests pass ✅
        ↓
Render pulls latest code and deploys
        ↓
Live site updates automatically

🧪 Continuous Integration (CI) — GitHub Actions

File: .github/workflows/ci.yml

On every push to main:

Python environment is created

Dependencies are installed from requirements.txt

Django tests are executed using python manage.py test

If any test fails → deployment is stopped

Automated Tests Included

The pipeline verifies:

Task creation works

Task completion works

Task deletion works

This ensures the application is always functional before deployment.

🚀 Continuous Deployment (CD) — Render

Render is connected to the GitHub repository.

When CI passes:

Render pulls the latest code

Installs dependencies

Runs the app using Gunicorn

Deploys the updated version automatically

🔐 Environment Variables (Production Best Practice)

Sensitive data is not stored in the code.

These are configured in Render:

SECRET_KEY

DEBUG

ALLOWED_HOSTS

This follows real-world production standards.

📦 Requirements

All dependencies are listed in requirements.txt, including:

Django

Gunicorn

🏁 Run Locally
pip install -r requirements.txt
python manage.py runserver


Visit: http://127.0.0.1:8000

🧑‍💻 Technologies Used

Python

Django

Git & GitHub

GitHub Actions

Render Cloud Platform

Gunicorn

Bootstrap

🎯 Learning Outcome

This project demonstrates understanding of:

Django web development

Database integration

Git version control

CI/CD pipeline creation

Automated testing

Cloud deployment practices used in industry

📌 Conclusion

This project simulates how real software teams build, test, and deploy applications using DevOps practices, ensuring reliability, automation, and production readiness.