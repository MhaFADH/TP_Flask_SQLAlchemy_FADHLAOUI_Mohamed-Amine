#FADHLAOUI MOHAMED-AMINE

from flask import Flask
from flask_migrate import Migrate
from .models import *
from .database import db
from .rtChambre import chambre_bp,main
from .rtReservation import reservation_bp
from .rtClient import client_bp


migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@db/hoteldb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)
    with app.app_context():
        db.create_all()

    migrate.init_app(app, db)

    app.register_blueprint(chambre_bp, url_prefix='/api/chambres')
    app.register_blueprint(reservation_bp, url_prefix='/api/reservations')
    app.register_blueprint(client_bp, url_prefix='/api/clients')
    app.register_blueprint(main)


    return app
