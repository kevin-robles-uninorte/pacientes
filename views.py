from flask import render_template, request

def indexView():
    if request.method == "POST":
        userName = request.form["userName"]
        userPassword = request.form["userPassword"]
    return render_template('index.html', userName=userName, userPassword=userPassword)

def loginView():
    return render_template('login.html')

def testView():
    return 'it works!'