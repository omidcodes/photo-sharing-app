
# Do not forget to change .env file in real environment.



# Django Photo Sharing App

This is a web application similar to a basic version of Instagram. It allows users to upload, view, comment on, and rate pictures.

## 📌 Features

- **User Authentication**: Users can register, log in, and log out.
- **Photo Upload**: Authenticated users can upload pictures along with optional metadata:
  - Title
  - Caption
  - Location (e.g., "Photo taken at: ...")
  - People present
- **Gallery View**: All uploaded pictures are displayed in a gallery view with:
  - Title, caption, location, people present
  - Uploaded by username
  - Paginated (9 pictures per page)
- **Rating System**: Users can rate each picture from 1 to 5. Average rating is calculated and shown. Duplicate ratings by the same user are updated.
- **Commenting**: Users can add comments under each picture. Comments include timestamp and username.
- **Responsive Design**: Layout is styled using Bootstrap and FontAwesome for icons.
- **Footer**: Displays creator name and LinkedIn profile.

## 👤 Developer

This website was designed and developed by **Omid Hashemzadeh**  
[LinkedIn Profile](https://www.linkedin.com/in/omid-hashemzadeh-2b3048113/)

## 🚀 Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies with `pip install -r requirements.txt`
4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

## 📝 License

This project is for educational and portfolio purposes.
