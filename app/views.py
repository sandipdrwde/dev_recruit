from flask import render_template, request, flash, redirect, url_for, session
from datetime import datetime
from werkzeug import secure_filename
from functools import wraps
import base64

from app import app, db
from app.models import ApplicationDetail, ApplicationStatus
import os, sys,gc


#=========================================================================================================================#
#===================================================== Login Wrap ========================================================#
#=========================================================================================================================#

def login_required(f):
    @wraps(f)
    def wrap(*args , **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first ...!")
            return redirect(url_for('admin_login'))
    return wrap

#=========================================================================================================================#
#===================================================== Role Wrap =========================================================#
#=========================================================================================================================#

def role_required(f):
    @wraps(f)
    def wrap(*args , **kwargs):
        if session['username'] == 'admin' :
            return f(*args, **kwargs)
        else:
            flash("You are not administrator ...!")
            return redirect(url_for('admin_login'))
    return wrap

#=========================================================================================================================#
#===================================================== Logout ============================================================#
#=========================================================================================================================#

@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been logged out ...!")
    gc.collect()
    return redirect(url_for('admin_login'))

#=========================================================================================================================#
#====================================================== Home Page ========================================================#
#=========================================================================================================================#

@app.route('/' , methods = ["GET","POST"])
def home():
    error = ''
    try:
        return render_template('home_page.html')

    except Exception as e:
    	exc_type, exc_obj, exc_tb = sys.exc_info()
        e = str(e) + str(exc_type) + str(exc_tb.tb_lineno)
        return render_template('home_page.html', error = e)

#=========================================================================================================================#
#====================================================== Application ======================================================#
#=========================================================================================================================#

@app.route('/apply/' , methods = ["GET","POST"])
def apply():
    error = ''
    try:
        if request.method == "POST":

            firstname = request.form['firstname'].encode('ascii','ignore')
            lastname = request.form['lastname'].encode('ascii','ignore')
            gender = request.form['gender'].encode('ascii','ignore')
            dob = request.form['dob'].encode('ascii','ignore')
            emailid = request.form['emailid'].encode('ascii','ignore')
            mobile = request.form['mobile'].encode('ascii','ignore')
            address = request.form['address'].encode('ascii','ignore')
            pincode = request.form['pincode'].encode('ascii','ignore')
            notice_period = request.form['notice_period'].encode('ascii','ignore')
            experience = request.form['experience'].encode('ascii','ignore')
            ctc = request.form['ctc'].encode('ascii','ignore')
            etc = request.form['etc'].encode('ascii','ignore')
            inputfile = request.files['inputfile']
            infile = base64.b64encode(inputfile.read())
            dob = datetime.strptime(dob, '%d/%m/%Y').strftime('%Y/%m/%d')
            # print firstname, lastname, gender, type(dob), pincode, notice_period, experience, ctc, etc, inputfile
            data = ApplicationDetail(first_name=firstname, last_name=lastname, gender=gender, dob=dob, email=emailid,
            mobile_number=mobile,address=address, pincode=pincode, notice_period=notice_period, experience=experience,
            current_ctc=ctc, upload_file=infile, expected_ctc=etc)
            db.session.add(data)
            db.session.commit()
            # if inputfile:
            #     infile = base64.b64encode(inputfile.read())
            #     cur.execute("UPDATE employee_info set (Profile_Pic) = (%s) WHERE emp_id = (%s);", [pic, emp_id])

            flash("Application submitted successfully")
            return redirect(url_for('apply'))

        return render_template('apply.html')

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        e = str(e) + str(exc_type) + str(exc_tb.tb_lineno)
        return render_template('apply.html', error = e)

#=========================================================================================================================#
#====================================================== Admin Login ======================================================#
#=========================================================================================================================#

@app.route('/admin/' , methods = ["GET","POST"])
def admin_login():
    error = ''
    try:
        # conn, cur  = connection()
        if request.method == "POST":

            userid = request.form['userid']
            password = request.form['password']

            if  userid == 'admin' and password == 'admin':

                session['logged_in'] = True
                session['userid'] = "admin"
                session['username'] = "admin"

                flash("You are logged in successfully.")
                return redirect(url_for("admin_page"))

            else:
                error = "Invalid credentials. Try again...!"
                return render_template('login_page.html', error = error)

        return render_template('login_page.html')

    except Exception as e:
    	error = "Invalid credentials. Try again...!"
    	exc_type, exc_obj, exc_tb = sys.exc_info()
        e = str(e) + str(exc_type) + str(exc_tb.tb_lineno)
        return render_template('login_page.html', error = e)

#=========================================================================================================================#	
#====================================================== Admin ============================================================#
#=========================================================================================================================#

@app.route('/admin_page/' , methods = ["GET","POST"])
@login_required
@role_required
def admin_page():
    error = ''
    try:
        data = ApplicationDetail.query.all()
        status_data = ApplicationStatus.query.all()
        app_id_list = [st.applicant_id for st in status_data]
        # data = ApplicationDetail.query.join(ApplicationStatus, ApplicationDetail.applicant_id==ApplicationStatus.id).all()
        return render_template('admin_page.html', data=data, status_data=status_data, app_id_list=app_id_list)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        e = str(e) + str(exc_type) + str(exc_tb.tb_lineno)
        return render_template('admin_page.html', error = e)


#=========================================================================================================================# 
#====================================================== view =============================================================#
#=========================================================================================================================#

@app.route('/view_application/<app_id>' , methods = ["GET","POST"])
@login_required
@role_required
def view_application(app_id=None):
    error = ''
    try:
        data = ApplicationDetail.query.filter(ApplicationDetail.applicant_id==app_id).first()
        # data = ApplicationDetail.query.join(ApplicationStatus, ApplicationDetail.applicant_id==ApplicationStatus.id).all()
        return render_template('view_application.html', data=data)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        e = str(e) + str(exc_type) + str(exc_tb.tb_lineno)
        return render_template('view_application.html', error = e)


#=========================================================================================================================# 
#====================================================== Status ===========================================================#
#=========================================================================================================================#

@app.route('/app_status/<app_id>/<status>/' , methods = ["GET","POST"])
@login_required
@role_required
def app_status(app_id=None, status=None):
    error = ''
    try:
        exist_id = ApplicationStatus.query.filter(ApplicationStatus.applicant_id==app_id).first()
        if exist_id:
            AppStatus = ApplicationStatus.query.filter(ApplicationStatus.applicant_id==app_id).first()
            AppStatus.status = status
            db.session.commit()
        else:
            data = ApplicationStatus(applicant_id=app_id, status=status)
            db.session.add(data)
            db.session.commit()

        if status == "accepted":
            flash("You have accepted the application")
        else:
            flash("You have rejected the application")

        return redirect(url_for("admin_page"))

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        e = str(e) + str(exc_type) + str(exc_tb.tb_lineno)
        return render_template('admin_page.html', error = e)
        
#=========================================================================================================================#
#====================================================== End ==============================================================#
#=========================================================================================================================#