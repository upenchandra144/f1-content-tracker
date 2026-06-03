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
12) In terminal use git remote add origin https://github.com/upenchandra144/f1-content-tracker.git, this helps to connect the folder files to this github repository
13) Rename the branch to main git branch -M main
14) Push using git push -u origin main