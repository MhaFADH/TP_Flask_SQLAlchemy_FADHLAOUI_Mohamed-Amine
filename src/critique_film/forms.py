#FADHLAOUI MOHAMED-AMINE

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,IntegerField
from wtforms.validators import DataRequired, Email


class InscriptionForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Inscription')


class AjoutFilmForm(FlaskForm):
    titre = StringField('Titre', validators=[DataRequired()])
    realisateur = StringField('Réalisateur')
    annee_sortie = IntegerField('Année de Sortie')
    genre = StringField('Genre')
    submit = SubmitField('Ajouter le Film')