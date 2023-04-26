from flask import Flask, render_template, request
import mysql.connector
#from forms import SignUpForm

app = Flask('app')

@app.route('/')
def welcome():
    return render_template(
        'welcome.html'
    )

@app.route('/form')
def form():
  return render_template(
    'form.html'
  )

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
  print(request.args, "firstName" in request.args)
  if "firstName" in request.args:
     sign_up(request.args.get("firstName"), request.args.get("lastName"), request.args.get("username"),
             request.args.get("email"), request.args.get("password"), request.args.get("balance"))

  return render_template(
    'signup.html',
    
  )

@app.route('/login', methods = ['GET', 'POST'])
def login():
  print(request.args, "username" in request.args)
  if "username" in request.args:
    log_in(request.args.get("userName"), request.args.get("password"))
    return render_template(
        'account.html'
    )




  return render_template(
    'login.html'
  )

@app.route('/menu')
def menu():
  return render_template(
    'menu.html'
  )

@app.route('/account', methods = ['GET', 'POST'])
def account():
  print(request.args, "firstName" in request.args)
  if "firstName" in request.args:
    modify_account(request.args.get("username"), request.args.get("firstName"), request.args.get("lastName"), request.args.get("email"), request.args.get("password"))

  return render_template(
    'account.html'
   )

    




def modify_account(username, firstName, lastName, email, password):
    if firstName and lastName and email and password: # check if all values are not empty or None
        connection = mysql.connector.connect(user="root", database="quickbanking", password="Hikmet1q.")
        connection.autocommit = True
        cursor = connection.cursor()

        modify = (f"""UPDATE account SET firstName = '{firstName}', lastName = '{lastName}', email = '{email}', password = '{password}' WHERE username = '{username}'""")

        cursor.execute(modify)

        connection.commit()
        cursor.close()
        connection.close()
    else:
        print("Error: One or more values are empty or None.")




def log_in(username, password):
  check = (f"""SELECT * FROM account WHERE userName = '{username}' AND password = '{password}'""")

  connection = mysql.connector.connect(user = "root", database = "quickbanking", password = "Hikmet1q.")
  connection.autocommit = True
  cursor = connection.cursor()

  cursor.execute(check)

  
  connection.close()



def sign_up(firstName, lastName, username, email, password,  balance):
  insert = (f"""INSERT INTO account (firstName, lastName, userName, email, password, balance) 
  VALUES ('{firstName}', '{lastName}', '{username}', '{email}', '{password}',  {balance})""")



  connection = mysql.connector.connect(user = "root", database = "quickbanking", password = "Hikmet1q.")
  connection.autocommit = True
  cursor = connection.cursor()

  cursor.execute(insert)

  cursor.close()
  connection.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

