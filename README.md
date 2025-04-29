
# 📸 Photo Sharing App (Django + Azure)

A full-stack Django application for sharing photos, with the ability to register/login, upload photos, rate, and comment. It's designed with scalability in mind using Azure cloud services and automated CI/CD via GitHub Actions.

---

## 🚀 Features

- User registration and login/logout support
- Upload images with metadata: title, caption, location, and tagged people
- View all uploaded pictures in a paginated gallery
- Rate pictures (0–5) and leave comments
- Store media files in Azure Blob Storage
- Use Azure SQL Database as backend
- Secure login with CSRF protection
- GitHub Actions for CI/CD deployment to Azure Web App

---

## 📦 Requirements

- Python 3.12
- Django 5.x
- Azure SQL Database (server + database created)
- Azure Blob Storage (container for media)
- Azure Web App (Linux, Python 3.12)
- `pip`, `virtualenv`

---

## 🧰 Local Development Setup

### 1. Clone the Project

```bash
git clone https://github.com/ohashemzadeh/photo-sharing-app.git
cd photo-sharing-app
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Project Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

```ini
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=your-db-host.database.windows.net
DB_PORT=1433

AZURE_STORAGE_ACCOUNT_NAME=yourstorageaccount
AZURE_STORAGE_ACCOUNT_KEY=yourstoragekey
AZURE_STORAGE_CONTAINER_NAME=media

CSRF_TRUSTED_ORIGINS=https://your-deployed-azure-site.azurewebsites.net
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) and login or register.

---

## ☁️ Azure Setup Guide

### 1. Azure SQL Database

- Use Azure Portal to create an SQL Server and database.
- Set firewall to allow your IP and GitHub Actions.
- Create admin username and password.
- Save all values for `.env`.

### 2. Azure Blob Storage

- Create a storage account and a container (e.g. `media`).
- Get the account key and name.
- Container access can be public or private (Django handles auth).

### 3. Azure Web App

- Create a Linux Web App for Python 3.12.
- Configure startup command (optional): `gunicorn MyDjangoProject.wsgi`
- Connect it to GitHub repo via Deployment Center.
- Add environment variables or use GitHub secrets.

### 4. Add `CSRF_TRUSTED_ORIGINS`

You **must** set your Azure Web App domain here, or CSRF will block login:

```ini
CSRF_TRUSTED_ORIGINS=https://your-web-app.azurewebsites.net
```

---

## 🔄 GitHub Actions Deployment

A complete workflow is included to:

- Build your Python environment
- Install `pyodbc` and Microsoft ODBC Driver 18
- Run Django migrations and collect static files
- Deploy to Azure Web App

### Required GitHub Secrets

Add these secrets to GitHub **(repository or environment scope)**:

- `SECRET_KEY`
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- `AZURE_STORAGE_ACCOUNT_NAME`, `AZURE_STORAGE_ACCOUNT_KEY`, `AZURE_STORAGE_CONTAINER_NAME`
- `AZUREAPPSERVICE_PUBLISHPROFILE_...`
- `CSRF_TRUSTED_ORIGINS` → `https://your-web-app.azurewebsites.net`

---

## 🧪 Local Test

After setting up:

```bash
python manage.py migrate
python manage.py runserver
```

You should be redirected to `/login/` when accessing `/` if unauthenticated.

---

## 🔐 Security Best Practices

- CSRF protection is enforced via `CSRF_TRUSTED_ORIGINS`
- Never disable CSRF middleware globally
- Avoid hardcoding `SECRET_KEY` in `settings.py`; always use environment variables

---

## 📁 Project Structure Highlights

- `users_app`: Registration, login, logout views
- `pictures_app`: Photo upload, gallery, rating, and comments
- `templates/`: HTML files for pages and forms
- `.github/workflows/`: CI/CD pipeline config for Azure

---

## 👤 Author

Designed & Developed by **Omid Hashemzadeh**  
[LinkedIn](https://www.linkedin.com/in/omid-hashemzadeh-2b3048113/)  
© 2025

---

## 📝 License

Licensed under the [MIT License](LICENSE).
