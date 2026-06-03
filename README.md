# F1 Content Tracker
Tracks YouTube video performance for Formula 1 race weekends.

## Setup
1) Create virtual environment: python -m venv venv
2) Activate: .\venv\Scripts\activate
3) Install dependencies:
4) Create requirements.txt / pip install -r requirements.txt
5) Create README.md
6) Run django-admin startproject backend . to create the backend folder which has folders like settings, urls, etc. | This creates manage.py  used for runserver, migrate, createsuperuser | settings.py which contains project configurations like Installed apps, databases, middleware | urls.py contains routes requests
7) We then create a app using python manage.py startapp videos, this automatically creates a folder which contains various files like models, tests, views etc.
8) Once add is created we create a .gitignore file so this makes sure that only required files are tracked and not all, check which files are tracked using git status
9) Verify working of django using manage.py runserver
10) Register app in backend/settings.py, this tells django that the app exists
11) Now go to github and create the repository
12) Also use git init because code is made locally, this turns regular directory in git repository
13) In terminal use git remote add origin https://github.com/upenchandra144/f1-content-tracker.git, this helps to connect the folder files to this github repository
14) Rename the branch to main git branch -M main
15) Push using git push -u origin main
16) Now when any changes save the local file, then git add ., then git commit -m and git push origin



17) Run python manage.py migrate, for creating django's built in table, tables like auth_user are very useful for users, this provides by default built in various user related fields
User Management Design Notes:
Django already provides:
Username, Password (securely hashed), Email, Login/Logout functionality, User authentication, Sessions, Permissions framework
This is the standard professional approach and avoids reinventing authentication.
UserProfile: Created by us to store additional business information.
id, user_id (OneToOneField to User), display_name, role, created_at, updated_at, Role choices:EDITOR, VIEWER
Why not store role directly in User?
We do not modify Django's internal User table. Instead we extend it using UserProfile. This is a common ERP and enterprise application pattern because additional fields can be added without affecting Django's authentication system.
Login Flow
User enters Username and Password.
Django checks credentials against the built-in User table.
If credentials are valid, Django logs the user in.
Application loads the corresponding UserProfile.
Role is checked.

18) We now create apps users and races and register them
19) Create models for each app
20) Install module pillow
21) Add name = 'apps.users' in users app instead of only users
22) Run python manage.py makemigrations
23) Check dependencies
24) Run python manage.py migrate for creating actual tables
25) Registering models in admin.py for each app from .models import Video, admin.site.register(Video)
26) Create superuser using python manage.py createsuperuser
27) Run python manage.py runserver and go to http://127.0.0.1:8000/admin/, for accessing the admin page