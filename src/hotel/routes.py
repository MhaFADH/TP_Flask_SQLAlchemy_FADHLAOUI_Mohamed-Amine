#FADHLAOUI MOHAMED-AMINE

from flask import Blueprint, render_template, request, jsonify
from .database import db
from .models import Client
from .models import Chambre



main = Blueprint('main', __name__)


@main.route('/')
def index():

    return "<h1>Api reservation chambre d'hotel, training python database manipulation</h1>"
    
@main.route('/api/chambres/disponibles', methods=['GET'])
def inscription():
    

        return render_template('index.html')

@main.route('/api/chambres', methods=['POST'])
def addRoom():
    body = request.get_json()

    new_room = Chambre(
        numero=body['numero'],
        type=body['type'],
        prix=body['prix']
    )

    db.session.add(new_room)

    try:
        db.session.commit()
        return jsonify({'success':True, 'message':'Room added successfully'})
    except:
        db.session.rollback()
        return jsonify({'success':False, 'message':'Error, Room not added, maybe it already exists'})
    
@main.route('/api/chambres/<id>', methods=['PUT'])
def editRoom(id):
        
    room = Chambre.query.get_or_404(id)

    body = request.get_json()
    
    room.numero=body['numero'],
    room.type=body['type'],
    room.prix=body['prix']

    try:
        db.session.commit()
        return jsonify({'success':True, 'message':'Room edited successfully'})
    except:
        db.session.rollback()
        return jsonify({'success':False, 'message':'Error, Room not edited, body not valid or room number already used'})

