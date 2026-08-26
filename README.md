## Project Structure

```text
attendance_tracker/
│
├── app.py                  # Flask application and routes
├── database.py             # MySQL database connection
├── schema.sql              # Database and table creation script
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment configuration
├── .gitignore              # Files excluded from Git
├── README.md               # Project documentation
│
├── static/
│   └── style.css           # Application styling
│
└── templates/
    ├── index.html          # Add participant page
    └── participants.html   # Participant list and attendance page
```

## Application Workflow

The application follows this basic flow:

```text
User
 │
 ├── Add Participant
 │       │
 │       ▼
 │    Flask
 │       │
 │       ▼
 │    MySQL
 │
 └── View Participants
         │
         ▼
      Flask
         │
         ▼
      MySQL
         │
         ▼
 Participant List + Attendance Summary
```

### Attendance Update

```text
Present / Absent button
          │
          ▼
   Flask POST request
          │
          ▼
    UPDATE MySQL
          │
          ▼
       Commit
          │
          ▼
   Redirect to Participants
```

---

# Database Setup

## 1. Install MySQL

Install MySQL and make sure the MySQL server is running.

You can use **MySQL Workbench** or the MySQL command-line client.

## 2. Create the Database

The project includes a `schema.sql` file that creates the required database and table.

Run the contents of:

```text
schema.sql
```

The schema creates:

```text
Database:
attendance_tracker

Table:
participants
```

The `participants` table contains:

| Column         | Type        | Description                   |
| -------------- | ----------- | ----------------------------- |
| id             | INT         | Auto-increment primary key    |
| participant_id | VARCHAR(20) | Unique participant identifier |
| name           | VARCHAR(50) | Participant name              |
| attendance     | ENUM        | Present or Absent             |

The `participant_id` column is unique to prevent duplicate participant registrations.

---

# Environment Configuration

The application uses environment variables for database credentials and the Flask secret key.

Create a `.env` file in the project root using `.env.example` as a template.

Example:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=attendance_tracker
SECRET_KEY=your_secret_key
```

Replace the placeholder values with your local MySQL credentials.

> **Important:** Never commit your actual `.env` file to GitHub. The `.gitignore` file is configured to exclude it.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Parth-Chouhan/attendance-tracker.git
```

Navigate into the project directory:

```bash
cd attendance-tracker
```

## 2. Create a Virtual Environment

On Windows:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

## 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file based on `.env.example`.

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=attendance_tracker
SECRET_KEY=your_secret_key
```

## 5. Set Up the Database

Run `schema.sql` using MySQL Workbench or the MySQL command line.

---

# Running the Application

Start the Flask development server:

```powershell
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000/
```

Open the URL in your browser.

---

# How to Use

## Add a Participant

1. Open the application.
2. Enter the participant's name.
3. Enter a unique Participant ID.
4. Click **Add Participant**.
5. A success message will be displayed after registration.

## View Participants

Click **View Participants** to see all registered participants.

The page displays:

* Participant ID
* Participant name
* Attendance status
* Present/Absent controls
* Total participant count
* Present count
* Absent count

## Update Attendance

Click **Present** or **Absent** next to a participant.

The attendance value is updated in MySQL and the summary is recalculated automatically.

---

# Validation and Error Handling

The application includes basic validation and error handling.

### Empty Fields

Participant name and Participant ID are required.

### Duplicate Participant ID

The database uses a `UNIQUE` constraint on `participant_id`.

If a duplicate ID is submitted, the application displays an appropriate error message instead of exposing a database error.

### Database Resources

Database cursors and connections are closed after database operations to prevent unnecessary open connections.

---

# Attendance Model

The current implementation tracks attendance for **one active session**.

Each participant has a single attendance status:

```text
Present
or
Absent
```

Updating the attendance status replaces the previous value.

A future version could introduce separate attendance records for multiple sessions or dates.

---

# Security

The project avoids storing sensitive credentials directly in the source code.

Database credentials and the Flask secret key are loaded from environment variables using `python-dotenv`.

The following files are intentionally excluded from Git:

```text
.env
venv/
__pycache__/
*.pyc
```

A `.env.example` file is provided with placeholder values so another developer can configure their own environment.

---

# Future Improvements

Possible future improvements include:

* Multiple attendance sessions
* Date-wise attendance tracking
* Attendance history
* Attendance percentage calculation
* Administrator authentication
* Search and filtering
* Export attendance reports
* CSV/PDF attendance reports
* Improved mobile responsiveness

---

# Learning Outcomes

This project demonstrates practical use of:

* Flask routing
* HTTP GET and POST requests
* HTML forms
* Jinja2 templates
* MySQL database operations
* SQL `INSERT`, `SELECT`, and `UPDATE`
* SQL aggregate functions such as `COUNT()` and `SUM()`
* Python exception handling
* Environment variables
* Git and GitHub
* Basic frontend styling with CSS

---

# Author

**Parth Chouhan**

Built as part of the **GFG task/project submission**.

```
```
