#FADHLAOUI MOHAMED-AMINE

import datetime
from flask import Blueprint, request, jsonify
from .database import db
from .models import Client



client_bp = Blueprint('client_bp', __name__)

@client_bp.route('', methods=['POST'])
def addClient():
  body = request.get_json()

  nom = body['nom']
  email = body['email']

  new_client = Client(
    nom=nom,
    email=email
  )

  db.session.add(new_client)

  try:
    db.session.commit()
    return jsonify({'success':True, 'message':'Client added successfully'})
  except:
    db.session.rollback()
    return jsonify({'success':False, 'message':'Error, Client not added, maybe it already exists'})
