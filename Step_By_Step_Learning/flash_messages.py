# Templatest Inheritance 

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
