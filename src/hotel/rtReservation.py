#FADHLAOUI MOHAMED-AMINE

import datetime
from flask import Blueprint, request, jsonify
from .database import db
from .models import Reservation
from .models import Chambre
from datetime import datetime
from sqlalchemy import and_



reservation_bp = Blueprint('reservation_bp', __name__)

@reservation_bp.route('', methods=['POST'])
def addReservations():
  body = request.get_json()
  id_client = body['id_client']
  id_chambre = body['id_chambre']
  date_arrivee = datetime.strptime(body['date_arrivee'], '%d-%m-%Y')
  date_depart = datetime.strptime(body['date_depart'], '%d-%m-%Y')

  reservations = Reservation.query.filter(Reservation.id_chambre == id_chambre,and_(Reservation.date_depart > date_arrivee,Reservation.date_arrivee < date_depart), Reservation.statut == 'RESERVED').count()

  if reservations > 0:
    return jsonify({'success':False, 'message':'Room already reserved for this period'})
  
  new_reservation = Reservation(
    id_client=id_client,
    id_chambre=id_chambre,
    date_arrivee=date_arrivee,
    date_depart=date_depart,
    statut='RESERVED'
  )

  db.session.add(new_reservation)

  try:
    db.session.commit()
    return jsonify({'success':True, 'message':'Reservation added successfully'})
  except:
    db.session.rollback()
    return jsonify({'success':False, 'message':'Error, Reservation not added, maybe it already exists'})

@reservation_bp.route('/<id>', methods=['DELETE'])
def deleteReservation(id):
        
    reservation = Reservation.query.get_or_404(id)

    try:
        db.session.delete(reservation)
        db.session.commit()
        return jsonify({'success':True, 'message':'Reservation canceled successfully'})
    except:
        db.session.rollback()
        return jsonify({'success':False, 'message':'Error, Reservation could not be canceled'})
    
@reservation_bp.route('', methods=['GET'])
def getReservation():
    
    date_arrivee = datetime.strptime(request.args.get('date_arrivee'), '%d-%m-%Y')
    date_depart = datetime.strptime(request.args.get('date_depart'),'%d-%m-%Y')
    

    reservations = Reservation.query.with_entities(Reservation.id_chambre).filter(and_(Reservation.date_depart > date_arrivee,Reservation.date_arrivee < date_depart), Reservation.statut == 'RESERVED').group_by(Reservation.id_chambre).all()
    reserved_rooms = []
    for reservation in reservations:
        reserved_rooms.append(reservation.id_chambre)

    free_rooms = Chambre.query.filter(~Chambre.id.in_(reserved_rooms)).all()
    roomList = []
    for room in free_rooms:
        roomList.append({'id':room.id,'numero':room.numero,'type':room.type,'prix':room.prix})

    return jsonify(roomList)
    
