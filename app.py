from flask import Flask, render_template, request, redirect, flash
import os
from database import get_db_connection
from dotenv import load_dotenv
from mysql.connector.errors import IntegrityError

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_participant():
    name = request.form["name"]
    participant_id = request.form["participant_id"]

    if not name.strip() or not participant_id.strip():
        flash("Name and Participant ID are required.", "error")
        return redirect("/")

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO participants (participant_id, name)
        VALUES (%s, %s)
    """

    values = (participant_id, name)

    try:
        cursor.execute(query, values)
        connection.commit()

    except IntegrityError:
        connection.rollback()
        flash(f"Participant ID {participant_id} already exists.", "error")
        return redirect("/")

    finally:
        cursor.close()
        connection.close()

    flash(f"Participant {name} added successfully!", "success")
    return redirect("/")

@app.route("/participants")
def participants():

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT id, participant_id, name, attendance
            FROM participants
        """)
        participants = cursor.fetchall()

        cursor.execute("""
            SELECT
                COUNT(*) AS total,
                SUM(attendance = 'Present') AS present,
                SUM(attendance = 'Absent') AS absent
            FROM participants
        """)

        summary = cursor.fetchone()

    finally:
        cursor.close()
        connection.close()

    return render_template(
        "participants.html",
        participants=participants,
        summary=summary
    )

@app.route("/attendance/<participant_id>", methods=["POST"])
def update_attendance(participant_id):

    status = request.form["status"]

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        UPDATE participants
        SET attendance = %s
        WHERE participant_id = %s
    """

    values = (status, participant_id)

    try:
        cursor.execute(query, values)
        connection.commit()

    finally:
        cursor.close()
        connection.close()

    return redirect("/participants")


if __name__ == "__main__":
    app.run(debug=True)