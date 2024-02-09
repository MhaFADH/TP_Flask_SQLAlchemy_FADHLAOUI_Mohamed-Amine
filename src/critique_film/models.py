#FADHLAOUI MOHAMED-AMINE

from .database import db
from datetime import datetime


class Auteur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    date_naissance = db.Column(db.DateTime, nullable=False)
    nationalite = db.Column(db.String(80), nullable=False)
    livres = db.relationship('Livre', backref='auteur')


class Livre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    date_publication = db.Column(db.DateTime,default=datetime.utcnow, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    id_auteur = db.Column(db.Integer, db.ForeignKey('auteur.id'))
    emprunts = db.relationship('Emprunt', backref='livre', uselist=True)


class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    emprunts = db.relationship('Emprunt', backref='utilisateur', lazy='dynamic')


class Emprunt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_utilisateur = db.Column(db.Integer, db.ForeignKey('utilisateur.id'))
    id_livre = db.Column(db.Integer, db.ForeignKey('livre.id'))
    date_emprunt = db.Column(db.DateTime,default=datetime.utcnow, nullable=False)
    date_retour = db.Column(db.DateTime, nullable=True)