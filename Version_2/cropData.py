from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
import base64
from markupsafe import Markup

app = Flask(__name__)

# MySQL Configuration for PythonAnywhere
app.config['MYSQL_HOST'] = 'naveenjayakrishna.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'naveenjayakrishn'
app.config['MYSQL_PASSWORD'] = 'organicfarming@hub'   # Replace with the one you set in the Databases tab
app.config['MYSQL_DB'] = 'naveenjayakrishn$organicFarmingHub'  # Note the $ in the db name!
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    cur = mysql.connection.cursor()  # Create cursor for each request
    if request.method == 'POST':
        if 'cropname' in request.form:
            crop_name = request.form['cropname']
            crop_details = request.form['aboutcrop']
            crop_image = request.files['cropimage']
            crop_binary_data = crop_image.read()
            crop_details = crop_details.replace('\n','<br>')
            sql = """INSERT INTO cropdata(cropname, details, crop_image) VALUES (%s, %s, %s)"""
            values = (crop_name, crop_details, crop_binary_data)
            cur.execute(sql, values)
            mysql.connection.commit()

        elif 'username' in request.form:
            username = request.form['username']
            feedback = request.form['feedback']
            sql = """INSERT INTO feedback(user_name, success_path) VALUES (%s, %s)"""
            values = (username, feedback)
            cur.execute(sql, values)
            mysql.connection.commit()

        elif 'message' in request.form:
            message = request.form['message']
            sql = """INSERT INTO siteFeedback(feedback) VALUES (%s)"""
            values = (message,)
            cur.execute(sql, values)
            mysql.connection.commit()

        return redirect(url_for('home'))

    # Fetch all crops
    cur.execute('SELECT cropname, details, crop_image FROM cropdata ORDER BY id DESC')
    crops = cur.fetchall()
    crop_list = []

    for crop in crops:
        crop_name = crop['cropname']
        crop_details = crop['details']
        crop_image = crop['crop_image']

        if isinstance(crop_image, bytes):
            crop_image_base64 = base64.b64encode(crop_image).decode('utf-8')
        else:
            crop_image_base64 = None

        crop_list.append({'name': crop_name, 'details': Markup(crop_details), 'image': crop_image_base64})

    #for crop in crops:
     #   crop_name, crop_details, crop_image = crop
      #  crop_image_base64 = base64.b64encode(crop_image).decode('utf-8') if crop_image else None
       # crop_list.append({'name': crop_name, 'details': crop_details, 'image': crop_image_base64})

    # Fetch all feedback
    cur.execute('SELECT user_name, success_path FROM feedback ORDER BY id DESC')
    feedbacks = cur.fetchall()
    feedback_list = [{'username': f['user_name'], 'feedback': f['success_path']} for f in feedbacks]

    # Fetch all feedback
   # cur.execute('SELECT user_name, success_path FROM feedback ORDER BY id DESC')
    #feedbacks = cur.fetchall()
    #feedback_list = [{'username': f[0], 'feedback': f[1]} for f in feedbacks]

    cur.close()
    return render_template('home.html', crops=crop_list, feeds=feedback_list)

