from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def hello_world():
    print(request.headers)
    return render_template(
        'welcome.html'
    )

@app.route('/form')
def form():
   return render_template(
      'form.html'
   )

@app.route('/signup')
def signup():
  return render_template(
    'signup.html'
  )

@app.route('/login')
def login():
  return render_template(
    'login.html'
  )

@app.route('/menu')
def menu():
  return render_template(
    'menu.html'
  )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

