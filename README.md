# dev_recruit

Recruitement portal
-----------------

  What is it?
  -----------
  This contains the Release-1(Iteration-1) and
  Recruitment site that exposes the following functionality:
  
    1] a page that allows anonymous users to submit applications
    2] a restricted administration page where admins can:
    3] view applications
    4] reject applications
    5] accept applications


  The Version
  -------------
  This is Recruitement site version 0.0.1 date of this release is 12-09-2018.

  Requirement:
  ------------------
    1]. Platform - Linux/ubuntu, python 2.7
    2]. Database - MySQL 5.7
    3]. Python Web framework - Flask


  Deployment steps:
  ------------------
  1]  Create database with name "recruitement_db"

    create database recruitement_db;
        
  2]  No need to create tables (Application using ORM)

  3]  Update the dev_recruit/sys_config.py file with database credentials
      like host, username, password, database name, 
      
  4]  Run the dev_recruit/requirements.txt file to install dependancies 
      
      pip install -r requirements.txt 


  Run the Application
  --------------------
  Go to the dev_recruit directory and run run.py
  
    python run.py
  
  Open browser and enter the following link
  
    1]. For anonymous user
        http://localhost:5000/

    2]. For Admin user
        http://localhost:5000/admin

      Admin credentials
      username - admin
      password - admin
     
 
