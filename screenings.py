from flask import Flask, render_template, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, validators

app = Flask(__name__)
app.secret_key = "Aiy2eijah5iel7ex9iex8ua9Queexa"
db = SQLAlchemy(app)


class Screenings(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	director = db.Column(db.String, nullable=False)
	release_year = db.Column(db.Integer, nullable=False)
	cast = db.Column(db.String, nullable=False)
	length = db.Column(db.Integer, nullable=False)
	synopsis = db.Column(db.String, nullable=False)
	screening_date = db.Column(db.String, nullable=False)
	screening_time = db.Column(db.String, nullable=False)
	screening_address = db.Column(db.String, nullable=False)
	host_name = db.Column(db.String, nullable=False)
	host_email = db.Column(db.String, nullable=False)
	host_phone = db.Column(db.String, nullable=False)


ScreeningForm = model_form(Screenings, base_class=FlaskForm, db_session = db.session)


class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, nullable=False, unique=True)
	passwordHash = db.Column(db.String, nullable=False)


	def setPassword(self, password):
		self.passwordHash = generate_password_hash(password)

	def checkPassword(self, password):
		return check_password_hash(self.passwordHash, password)


class UserForm(FlaskForm):
	email = StringField("email", validators=[validators.email()])
	password = PasswordField("password", validators=[validators.InputRequired()])


def currentUser():

	try:
		uid = int(session["uid"])
	except:
		return None

	return Users.query.get(uid)


app.jinja_env.globals["currentUser"] = currentUser



def loginRequired():
	if not currentUser():
		abort(403)


@app.route("/user/login", methods=["GET", "POST"])
def loginView():

	form = UserForm()

	if form.validate_on_submit():

		email = form.email.data
		password = form.password.data

		user = Users.query.filter_by(email=email).first()

		if not user:
			flash("Login failed")
			print("User does not exist")
			return redirect("/user/login")

		if not user.checkPassword(password):
			flash("Login failed")
			print("Incorrect password")
			return redirect("/user/login")


		session["uid"] = user.id


		flash("Login successful")
		return redirect("/nowshowing")

	return render_template("login.html", form=form)


@app.route("/user/register", methods=["GET", "POST"])
def registerView():

	form = UserForm()

	if form.validate_on_submit():
		email = form.email.data
		password = form.password.data

		if Users.query.filter_by(email=email).first():
			flash("User already exists -- Please log in")
			return redirect("/user/login")

		user = Users(email=email)
		user.setPassword(password)

		db.session.add(user)
		db.session.commit()

		flash("Registration successful -- You can now log in")
		return redirect("/user/login")


	return render_template("register.html", form=form)



@app.route("/user/logout")
def logoutView():

	session["uid"] = None
	flash("You have logged out")
	return redirect("/nowshowing")



@app.before_first_request
def initDB():

	db.create_all()



@app.errorhandler(404)
def custom404(e):
	return render_template("404.html")


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/screening/<int:id>/edit", methods=["GET", "POST"])
@app.route("/screening/new", methods=["GET", "POST"])
def addView(id=None):

	loginRequired()

	screening = Screenings()
	if id:
		screening = Screenings.query.get_or_404(id)
	form = ScreeningForm(obj=screening)

	if form.validate_on_submit():
		form.populate_obj(screening)
		db.session.add(screening)
		db.session.commit()

		flash("Movie Screening Added")
		return redirect("/nowshowing")

	return render_template("new.html", form=form)



@app.route("/screening/<int:id>/delete")
def deleteView(id):

	loginRequired()

	screening = Screenings.query.get_or_404(id)
	db.session.delete(screening)
	db.session.commit()

	flash("Screening deleted")
	return redirect("/nowshowing")


@app.route("/nowshowing")
def indexView():
	screeninglist = Screenings.query.all()
	return render_template("nowshowing.html", screeninglist=screeninglist)


if __name__ == "__main__":
	app.run()
