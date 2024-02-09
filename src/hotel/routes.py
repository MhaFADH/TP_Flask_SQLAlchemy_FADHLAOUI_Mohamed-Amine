#FADHLAOUI MOHAMED-AMINE

from flask import Blueprint, render_template
from .database import db
from .models import Client



main = Blueprint('main', __name__)


@main.route('/')
def index():

    # auteurs = Client.query.all()
    # tabl = []

    # for auteur in auteurs:
    #     tabl.append(f"<h1>auteur{auteur.emprunts.date_emprunt}</h1>")

    # mainstr = ''.join(tabl)

    return "<h1>hello world</h1>"
    
# @main.route('/inscription', methods=['GET', 'POST'])
# def inscription():
#     form = InscriptionForm()
#     # opérations pour enregistrer le formulaire
#     if form.validate_on_submit():

#         new_user = Client(
#             nom=form.nom.data,
#             email=form.email.data,
#         )

#         db.session.add(new_user)
#         db.session.commit()

#         return render_template('index.html')


