from flask import Flask, render_template, redirect, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, DEFAULT_IMAGE_URL
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "supersecret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQL_TRACK_MODIFICATIONS'] = False

toolabr= DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route("/")
def home():
    """Show pets list"""
    pets = Pet.query.all()
    return render_template("home.html", pets = pets)


@app.route("/add", methods=["GET","POST"])
def add_pet():
    """Show add pet form & handle form data"""
    form = AddPetForm()
    if form.validate_on_submit():
        data = {key:value for key, value in form.data.items() if key != "csrf_token"}

        if not data.get("photo_url"):
            data["photo_url"] = DEFAULT_IMAGE_URL

        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("pet_add_form.html", form=form, errors =form.errors)
    

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Show edit pet form & handle form data"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()

        return redirect(url_for('home'))
    
    else: 
        return render_template("pet_edit_form.html", pet=pet, form=form)