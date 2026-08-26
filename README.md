# Attendance Tracker

A simple web-based attendance management system built using Flask, Python, and MySQL.

## Features

- Add new participants
- Assign a unique Participant ID
- View all registered participants
- Mark participants as Present or Absent
- Display total participants
- Display total Present and Absent participants
- Prevent duplicate Participant IDs
- Display success and error messages
- Simple responsive user interface

## Technologies Used

- Python
- Flask
- MySQL
- HTML
- CSS
- Jinja2
- mysql-connector-python
- python-dotenv

## Project Structure

```text
attendance_tracker/
│
├── app.py
├── database.py
├── schema.sql
├── requirements.txt
├── .env.example
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    └── participants.html

Database Setup
Install MySQL.
Open MySQL Workbench or the MySQL command line.
Run the contents of schema.sql.

The schema creates the attendance_tracker database and the participants table.

Environment Setup

Create a .env file in the project root using .env.example as a template.

Example:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=attendance_tracker
SECRET_KEY=your_secret_key

Do not commit the actual .env file to GitHub.

Installation

Clone the repository and navigate into the project directory.

Create a virtual environment:

python -m venv venv

Activate it.

Windows
venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt
Running the Application

Start the Flask application:

python app.py

Then open:

http://127.0.0.1:5000/
How It Works

Participants are stored in the MySQL database.

The Flask backend handles:

Participant registration
Database queries
Attendance updates
Attendance summary
Validation and error handling

The frontend uses HTML and CSS to display the application interface.

Attendance

The current implementation tracks attendance for a single active session. A participant's Present/Absent status can be updated using the attendance buttons.

Security

Database credentials and the Flask secret key are stored in environment variables using .env.

The actual .env file is excluded from Git using .gitignore.

Future Improvements

Possible future improvements include:

Support for multiple attendance sessions
Attendance history
Date-wise attendance reports
Authentication for administrators
Export attendance reports

---

## One thing I want you to notice

We're **not putting your actual database credentials in the README**.

The README only shows:

```text
DB_PASSWORD=your_mysql_password