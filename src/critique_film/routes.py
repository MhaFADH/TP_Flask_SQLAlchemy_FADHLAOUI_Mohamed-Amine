#FADHLAOUI MOHAMED-AMINE

from flask import Blueprint, render_template
from .forms import InscriptionForm
from .forms import AjoutFilmForm
from .database import db
from .models import Utilisateur
from .models import Auteur
from .models import Livre
from .models import Emprunt



main = Blueprint('main', __name__)


@main.route('/')
def index():

    auteurs = Utilisateur.query.all()
    tabl = []

    for auteur in auteurs:
        tabl.append(f"<h1>auteur{auteur.emprunts.date_emprunt}</h1>")

    mainstr = ''.join(tabl)

    return "<h1>hello world</h1>" + mainstr
    # new_auteur = Auteur(
    #     nom='Stephen King',
    #     date_naissance='1947-09-21',
    #     nationalite='USA'
    # )

    # new_livre = Livre(
    #     titre='Ça',
    #     genre='Horreur',
    #     id_auteur=1,
    #     date_publication='1986-09-15',
    # )

    # db.session.add(new_auteur)
    # db.session.add(new_livre)

    # db.session.commit()

    # new_utilisateur1 = Utilisateur(
    #     nom='Carolyn Blair',
    #     email='bobga@epilbat.hr'
    # )
    # new_utilisateur2 = Utilisateur(
    #     nom='Linnie Terry',
    #     email='lowoliub@fenin.kh'
    # )
    # new_utilisateur3 = Utilisateur(
    #     nom='Dennis Adkins',
    #     email='dikelofa@ekfapri.eg'
    # )
    # new_utilisateur4 = Utilisateur(
    #     nom='Manuel Schwartz',
    #     email='puros@zan.tl'
    # )

    # objects = [new_utilisateur1, new_utilisateur2, new_utilisateur3, new_utilisateur4]

    # db.session.add_all(objects)

    # db.session.commit()

    # new_emprunt = Emprunt(
    #     id_utilisateur=1,
    #     id_livre=1
    # )

    # db.session.add(new_emprunt)
    # db.session.commit()


    return render_template('index.html')

@main.route('/inscription', methods=['GET', 'POST'])
def inscription():
    form = InscriptionForm()
    # opérations pour enregistrer le formulaire
    if form.validate_on_submit():

        new_user = Utilisateur(
            nom=form.nom.data,
            email=form.email.data,
        )

        db.session.add(new_user)
        db.session.commit()

        return render_template('index.html')
    return render_template('inscription.html', form=form)


