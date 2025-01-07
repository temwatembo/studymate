StudyMate: A Homework Tracking and Study Assistant

StudyMate is a Django-based project aimed at helping students track and manage their homework and study schedules. It provides a user-friendly platform to organize tasks, set deadlines, and monitor study progress.

 Features
- Add, update, and delete homework tasks.
- Set deadlines and task priorities.
- Receive reminders for deadlines.
- Track study progress visually.

 Folder Structure
```
studymate-main/
|-- static/               # Static assets (CSS, JS, images)
|-- templates/            # HTML templates
|-- studymate/            # Main Django application
    |-- settings.py       # Django settings
    |-- urls.py           # URL configurations
    |-- models.py         # Database models
    |-- views.py          # Views handling requests
|-- manage.py             # Django management script
```

 Tools Used
- Django 4.x
- Bootstrap 5 for front-end styling
- SQLite for local database

 Framework and Tools Versions
- Django: 4.2
- Python: 3.11
- Bootstrap: 5.3

 Requirements
- User-friendly interface for task management.
- Deadline tracking with reminders.
- Scalable design for future features.

 Start Commands
To run the project locally:
1. Clone the repository:
   ```bash
   git clone <repo-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd studymate-main
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
5. Open your browser and go to `http://127.0.0.1:8000/`.

  Future Enhancements
- Integration with Google Calendar.
- Collaborative study groups.
- Mobile application development

