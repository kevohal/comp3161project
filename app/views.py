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
            
            #get the username and password of person
            username = form.username.data
            password = form.password.data
 
            #change to mysql
            user = UserProfile.query.filter_by(username=username).first()

            if user is not None and check_password_hash(user.password, password):
                remember_me = False 

                if 'remember_me' n request.form:
                    remember_me = True


            login_user(user)
            flash('You have successfully logged in.', 'success')

            next_page = request.args.get('next')
            return redirect(next_page or url_for("secure_page"))
        else:
            flash('Incorrect credentials entered. Username or password is incorrect.', 'danger')

        flash_errors(form)

        return render_template("login.html", form-form)

            
@app.route('/logout')
def logout():
    logout_user()
    flash('You have been successfully logged out.', 'danger')
    return redirect(url_for('home'))



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


#placeholder retrieving the courses from cv file 
@app.route('/courses/')
def courses ():
    return render_template ('SELECT * FROM Courses')

# create course 
@app.route('/courses/create')
def create ():
    

@app.route('/courses/register')
def register ():



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

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")