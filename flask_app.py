# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/user")
# def user():
#     name = request.args.get("name")
#     age = request.args.get("age")

#     return f"Hello {name}, your age is {age}" #---------------


# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/user")

# def user():
#     name = request.args.get("name")
#     price = request.args.get("price")

#     return f"{name} your laptop price is {price}".  #-------------

# from flask import Flask, request, render_template

# app = Flask(__name__)


# @app.route("/")
# def home():
#     return render_template("login.html")


# @app.route("/login", methods=["POST"])
# def login():

#     username = request.form.get("username")
#     password = request.form.get("password")

#     return f"Username: {username}, Password: {password}" # -----------

# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route("/profile")

# def profile():
    # name = "Yogesh Mandawat"
    # age = 21
    # skill = "ML Engineer"


    # return render_template("profile.html", name = name, age = age, skill = skill) #-----------

# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route("/skills")
# def skills():

#     products = [
#         "laptop",
#         "mouse",
#         "keyboard",
#         "moniter"
#     ]

#     return render_template("skills.html", skills=products) #-------------------

# from flask import Flask, render_template, request

# app = Flask(__name__)


# @app.route("/college", methods=["GET", "POST"])
# def college():

#     if request.method == "POST":

#         name = request.form.get("name")
#         marks = int(request.form.get("marks"))

#         if marks >= 60:
#             result = "You are eligible for admission."
#         else:
#             result = "You are not eligible for admission."

#         return render_template(
#             "college.html",
#             name=name,
#             marks=marks,
#             result=result
#         )

#     return render_template("college.html") #--------------------

# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route("/")
# def home():
#     return render_template("about.html")


# if __name__ == "__main__":
#     app.run(debug=True)

##--------------------------------------

# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/college", methods = ["GET", "POST"])

# def college():

#     if request.method == "POST":

#         name = request.form.get("name")
#         marks = request.form.get("marks")

#         if not name:
#             return "Please enter name"

#         if not marks:
#             return "Please enter marks"

#         marks = int(marks)

#         if(100 < marks < 0):
#             return "Please Enter Valid Marks"

#         if(marks > 80):
#             result = "Excellent.."
        
#         elif(80 > marks > 60):
#             result = "Good.."

#         elif(60 > marks > 40):
#             result = "Poor.."

#         else:
#             result = "Better luck Next Time.."

#         return render_template(
#             "college.html",
#             name = name,
#             marks = marks,
#             result = result)


#     return render_template("college.html") 

##-----------------------------

# from flask import Flask, render_template, request, url_for, redirect

# app = Flask(__name__)

# @app.route("/college", methods = ["POST", "GET"])

# def college():

#     if request.method == "POST":

#         name = request.form.get("name")
#         marks = request.form.get("marks")

#         marks = int(marks)

#         if not name:
#             return "Name Required"

#         if not marks:
#             return "Marks Required"

#         if(0 > marks > 100):
#             return "Please Enter Valid Marks"
        
#         #result = "You are passed" # when i used render templates..
#         #return render_template("college.html", name = name, marks=marks, result = result) 
    
#         # it will directly open the new page but function name is required
#         return redirect("result")
#     return render_template("college.html")

# @app.route("/result")
# def result():
#     return " Your result will be shown here...."

# @app.route("/yogesh") # its for checking the redirect method
# def yogesh():
#     return "Hey this is yogesh bhau mandawat"

from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)

app.secret_key = "my-secret-key"

@app.route("/login", methods = ['GET', 'POST'])

def login():

    if request.method == 'POST':

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "yogesh" and password == "1234":

            session['username'] = username

            flash("Login Succefilly...")

            return redirect(url_for('dashboard'))

        flash("Invalid Username...")

        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/dashboard")

def dashboard():

    if "username" not in session:

        return redirect(url_for('login'))

    username = session.get("username")

    return f"Welcome {username}!"

@app.route("/logout")

def logout():

    session.pop("username", None)

    flash("You have been loged out...")

    return redirect(url_for("login"))
