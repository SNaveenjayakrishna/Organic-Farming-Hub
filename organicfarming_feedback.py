from flask import Flask, request, render_template, redirect
import mysql.connector
import base64

app = Flask(__name__)

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Naveen@1234',
    database = 'organicFarmingHub'
)

cursor = db.cursor()

@app.route('/', methods = ['GET', 'POST'])
def storefeedback():
    if request.method == 'POST':
        username = request.form['username']
        feedback = request.form['feedback']

        sql = """INSERT INTO feedback(user_name, user_feedback) VALUES (%s, %s)"""
        values = (username, feedback)

        cursor.execute(sql, values)
        db.commit()
    cursor.execute('SELECT user_name, user_feedback FROM feedback')
    feedbacks = cursor.fetchall()  # Fetch all records

    # Convert binary image data to Base64
    feedback_list = []
    for feed in feedbacks:
        username, feedback = feed
        feedback_list.append({
            'username':username,
            'feedback':feedback,
        })

    return render_template('home.html', feeds=feedback_list)


if __name__ == '__main__':
    app.run(debug=True, port=5001)