from flask import Flask, render_template, request
import mysql.connector
from flask import send_file
#from forms import SignUpForm

app = Flask('app')

@app.route('/')
def welcome():
    return render_template(
        'welcome.html'
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
  print(request.args, "firstName" in request.args, "newB" in request.args, "removedB" in request.args, "password" in request.args, "check_userName" in request.args)
  if "newB" in request.args:
    deposit(request.args.get("userName"), request.args.get("newB"))
  if "firstName" in request.args:
    modify_account(request.args.get("username"), request.args.get("firstName"), request.args.get("lastName"), request.args.get("email"), request.args.get("password"))
  if "removedB" in request.args:
    withdraw(request.args.get("userName"), request.args.get("removedB"))
  if "password" in request.args:
    delete_account(request.args.get("userName"), request.args.get("password"))
  if "check_userName" in request.args:
    check_balance(request.args.get("check_userName"))
  


  return render_template(
    'account.html'
   )






def check_balance(check_userName):
  connection = mysql.connector.connect(user="root", database="quickbanking", password="Hikmet1q.")
  connection.autocommit = True
  cursor = connection.cursor()

  check_bal = f"""SELECT balance FROM account WHERE userName = '{check_userName}';"""

  cursor.execute(check_bal)

  bal = cursor.fetchone()


  connection.commit()
  cursor.close()
  connection.close()

  
  




def delete_account(userName, password):
  connection = mysql.connector.connect(user="root", database="quickbanking", password="Hikmet1q.")
  connection.autocommit = True
  cursor = connection.cursor()

  delete = f"""DELETE FROM account WHERE userName = '{userName}' and password = '{password}';"""

  cursor.execute(delete)

  connection.commit()
  cursor.close()
  connection.close()



def withdraw(userName, removedB):
  connection = mysql.connector.connect(user="root", database="quickbanking", password="Hikmet1q.")
  connection.autocommit = True
  cursor = connection.cursor()

  withdraw = f"""UPDATE account SET balance = balance - {removedB} WHERE userName = '{userName}';"""

  cursor.execute(withdraw)

  connection.commit()
  cursor.close()
  connection.close()



def deposit(userName, newB):
  connection = mysql.connector.connect(user="root", database="quickbanking", password="Hikmet1q.")
  connection.autocommit = True
  cursor = connection.cursor()

  deposit = f"""UPDATE account SET balance = balance + {newB} WHERE userName = '{userName}';"""

  cursor.execute(deposit)

  connection.commit()
  cursor.close()
  connection.close()



def modify_account(username, firstName, lastName, email, password):
  connection = mysql.connector.connect(user="root", database="quickbanking", password="Hikmet1q.")
  connection.autocommit = True
  cursor = connection.cursor()

  modify = (f"""UPDATE account SET firstName = '{firstName}', lastName = '{lastName}', email = '{email}', password = '{password}' WHERE username = '{username}'""")

  cursor.execute(modify)

  connection.commit()
  cursor.close()
  connection.close()




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

