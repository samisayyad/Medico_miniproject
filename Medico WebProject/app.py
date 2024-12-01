from flask import Flask, render_template,  request, redirect

from utils.db import db
from models.medic import *


app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medic.db'

@app.route('/')
def index():
    patient = Patients.query.all()
    return render_template('index.html',  content=patient)

@app.route('/patients')
def patients():
    return render_template('patients.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/help')
def help():
    return render_template('help.html')


db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/submit", methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    patient_age = form_data.get('patient_age')
    patient_bmi = form_data.get('patient_bmi')
    patient_children = form_data.get('patient_children')
    patient_charges = form_data.get('patient_charges')


    patient = Patients.query.filter_by()
    if not patient:
        patient = Patients(age=patient_age, bmi=patient_bmi, children=patient_children, charges=patient_charges)
        db.session.add(patient)
        db.session.commit()

    print("sumitted successfully")
    return redirect('/')

if __name__ =='__main__':
    app.run(host='127.0.0.1',port=5003,debug=True)
