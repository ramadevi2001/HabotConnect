# HabotConnect


### Local Setup Guide
1. Install Softwares: 
    1. Python 
    2. PostgreSQL & PgAdmin
    3. Visual Studio Code editor
    4. Postman
2. Clone the repository using the the following command: git clone https://github.com/ramadevi2001/HabotConnect.git
3. Setup Database :
    1. create database using the pgadmin
    2. In the code go to setttings.py file change your database configuration (database, username, password)

3. Virtual Enviroment and package installation
   1. create virtual environment using the command `python -m venv env`
   2. activate virtual environment using the command `.\env\Scripts\activate` for windows, for mac and linux using the command `source env/bin/activate`
   3. install the packages using the command `pip install -r requirements.txt`

4. Migrations and creating the tables in database
   1. please make sure your database credentials one more time
   2. change to project directory using the command `cd employee_management`
   3. run the command for makign the migrations `python manage.py makemigrations`
   4. run the command for migrting and making the database tables `python manage.py migrate`
5. Running the server and checking the APIS
   1. By the step above create all the tables required, now run the application or server using the command `python manage.py runserver`
   2. Go the postman import this collection [(https://api.postman.com/collections/34747528-887d6646-c143-4584-9895-fc896f00f9da?access_key=PMAT-01JBQM9GPGGGM916JWSHX4GGX7)]
   3. create enviroment postman with variables url as `http://localhost:8000`, token value you can steup when you logged in
   4. call the create API You will get the result following image<img width="946" alt="image" src="https://github.com/ramadevi2001/HabotConnect/issues/2">

   5. Congrats your backend setup for this project is done.


   ### For running the Testcases 
   use this command **python manage.py test**




### Aditional Commands
1. whenever installed new package is update the requirements.txt using the command `pip freeze > requirements.txt` make sure your virtual environment is active before running this command.




