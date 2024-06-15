from flask import Flask, render_template, request, redirect, url_for
import os
from tomato_disease import detect
from tomato_disease import diseaseseverity
from expertsys import tomato_databaseextract as tomdb
import expert_distance as exp
import handle_db as db
import requests



app = Flask(__name__)

# Define the path to the folder where uploaded images will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

USER = None

API_KEY = '3a5d4128143d053a6140772a71d82d0f'

LAT, LON = None, None

DISEASE = None




@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    elif request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password !=  confirm_password:
            return render_template("register.html", message="Passwords do not match!")
        
        db.insert_farmer(phone, name, password)

        return render_template("login.html", message="Registered Successfully!")
        
        
@app.route('/expert')
def expert_index():
    return render_template('expert_login.html')

@app.route('/farmer_login', methods=['GET', 'POST'])
def farmer_login():
    global USER
    if request.method == "POST":
        phonenumber = request.form.get("phonenumber")
        password = request.form.get("password")

        if phonenumber is None or password is None:
            return render_template('login.html', message="Invalid Credentials")
        elif db.get_login_details_farmer(phonenumber, password):
            USER = phonenumber
            return redirect(url_for('homepage'))
        return render_template('login.html', message="Invalid Credentials")
    
@app.route('/detect_disease')
def detect_disease():
    return render_template("index.html")

@app.route('/home')
def homepage(msg=""):
    return render_template("home.html", message=msg)

@app.route('/upload', methods=['POST'])
def upload():
    global DISEASE
    # Check if the 'image' file is in the request
    if 'image' not in request.files:
        return "No file part"

    file = request.files['image']

    # If the user does not select a file, the browser submits an empty file
    if file.filename == '':
        return "No selected file"

    # Save the uploaded file to the UPLOAD_FOLDER
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        classname, confidence = detect.detect(filename)

        if "healthy" in classname.lower():
            DISEASE = "Healthy"
            result = f"Leaf is healthy"
        elif "late" in classname.lower():
            DISEASE = "Late Blight"
            severity = diseaseseverity.calculate_disease_severity(filename)
            result = f"Leaf is infected with Late Blight disease. Severity: {severity:.2f}%"
        elif "early" in classname.lower():
            DISEASE = "Early Blight"
            severity = diseaseseverity.calculate_disease_severity(filename)
            result = f"Leaf is infected with Early Blight disease. Severity: {severity:.2f}%"

        # Replace the following line with your disease detection result
        # result = f"Leaf is infected with {classname} disease and has {confidence}% accuracy"

        return result


@app.route("/update_location", methods=["POST"])
def update_location():
    global LAT, LON
    data = request.get_json()
    # print(LAT, LON)

    lat, lon = data.get("latitude"), data.get("longitude")

    LAT, LON = lat, lon
    # print(LAT, LON)

    db.update_location_farmer(USER, f"({LAT}, {LON})")

    return "Location updated successfully!"

def get_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    # print(url)
    response = requests.get(url)
    data = response.json()
    return data

def get_3_day_forecast():
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

@app.route("/weather_data", methods=["GET", "POST"])
def weather_data():
    # print(LAT)
    # print(LON)
    if LAT is None or LON is None:
        return homepage("Please enable location access!")
    
    weather_data = None
    forecast_data = None
    weather_data = get_weather_data()
    forecast_data = get_3_day_forecast()

    return render_template("weatherpage.html", city=weather_data.get("name"), weather_data=weather_data, forecast_data=forecast_data)

@app.route("/recommendations", methods=["GET"])
def recommendations():
    disease_name = DISEASE
    if disease_name is None:
        return render_template("recommend.html", message="No disease data available")
    else:
        result = tomdb.get_condition_data(disease_name)
        return render_template("recommend.html", data=result)
    

@app.route("/view_experts", methods=["GET"])
def get_experts():

    class Expert:
        def __init__(self, phone, name):
            self.phone = phone
            self.name = name

    phone_number = USER

    results = exp.get_farmer_and_closest_experts(phone_number)

    data = []

    for result in results:
        data.append(Expert(result[0], result[1]))

    return render_template("display_experts.html", experts = data)



@app.route("/update_location_expert", methods=["POST", "GET"])
def update_location_expert():
    data = request.get_json()

    lat, lon = data.get("latitude"), data.get("longitude")

    db.update_location_expert(USER, f"({LAT}, {LON})")

    return "Location updated successfully!"

@app.route("/expert_login", methods=["GET", "POST"])
def expert_login():
    global USER
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email is None or password is None:
            return render_template("expert_login.html", message="Please fill all the fields!")
        elif db.get_login_details_expert(email, password):
            USER = email
            return redirect(url_for('expert_home'))
        return render_template("expert_login.html", message="Invalid Credentials")

@app.route("/expert_home")
def expert_home():
    return render_template("expert_homepage.html")

if __name__ == '__main__':
    app.run(debug=True)
