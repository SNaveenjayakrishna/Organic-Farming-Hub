from flask import Flask, request, render_template, redirect, url_for, jsonify
from markupsafe import Markup
import mysql.connector
import base64

app = Flask(__name__)

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Naveen@1234',
    database = 'organicFarmingHub'
)


@app.route('/', methods=['GET', 'POST'])
def home():
    cursor = db.cursor()
    if request.method == 'POST':
        if 'cropname' in request.form:
            crop_name = request.form['cropname']
            crop_details = request.form['aboutcrop']
            crop_image = request.files['cropimage']
            crop_binary_data = crop_image.read()
            crop_details = crop_details.replace('\n','<br>')
            sql = """INSERT INTO cropdata(cropname, details, crop_image) VALUES (%s, %s, %s)"""
            values = (crop_name, crop_details, crop_binary_data)
            cursor.execute(sql, values)
            db.commit()

        elif 'username' in request.form:
            username = request.form['username']
            feedback = request.form['feedback']
            sql = """INSERT INTO feedback(user_name, user_feedback) VALUES (%s, %s)"""
            values = (username, feedback)
            cursor.execute(sql, values)
            db.commit()
        return redirect(url_for('home'))

    # Fetch all crops
    cursor.execute('SELECT id, cropname, details, crop_image, entryTime FROM cropdata ORDER BY id DESC')
    crops = cursor.fetchall()
    crop_list = []
    for crop in crops:
        id, crop_name, crop_details, crop_image, entryTime = crop
        crop_image_base64 = base64.b64encode(crop_image).decode('utf-8') if crop_image else None
        crop_list.append({'id' : id, 'name': crop_name, 'details': Markup(crop_details), 'image': crop_image_base64, 'entryTime':entryTime})

    # Fetch all feedback
    cursor.execute('SELECT user_name, user_feedback, entryTime FROM feedback ORDER BY id DESC')
    feedbacks = cursor.fetchall()
    feedback_list = [{'username': f[0], 'feedback': f[1], 'entryTime': f[2]} for f in feedbacks]
    cursor.close()
    return render_template('home.html', crops=crop_list, feeds=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)