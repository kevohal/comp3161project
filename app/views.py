from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash 
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LofinForm
from app.models import UserProfile
from werkzeug.security import check_password_hash


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if current_user.is_authenticated:
                return redirect(url_for('secure_page'))






@app.route('/courses/')


@app.route('/courses/create')


@app.route('/courses/register')



@app.route('/courses/members')



@app.route('/events/')


@app.route('/events/create/')


@app.route('/forums/')


@app.route('/discussion/')


@app.route('/coursecontent/')


@app.route('/courses/assignments/')


@app.route('/reports/courses50/')


@app.route('/reports/students5/')


@app.route('/reports/lecturers3/')


@app.route('/reports/enrolled10/')


@app.route('/reports/averages10/')