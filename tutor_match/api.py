# -*- coding: utf-8 -*-

from app import db
from models.tutors import Tutors

from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError

api = Blueprint('api', __name__, url_prefix='/api')


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@api.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@api.route('/tutors', methods = ['GET'])
def get():
    tutors = Tutors.query
    
    id = request.args.get('id')
    name = request.args.get('name')
    document_no = request.args.get('document_no')
    
    if id:
        tutors = tutors.filter_by(id=id)
    if name:
        tutors = tutors.filter_by(name=name)
    if document_no:
        tutors = tutors.filter_by(document_no=document_no)
    
    data = [tutor.serialize() for tutor in tutors.all()]
    
    return jsonify(data)

@api.route('/tutors/<id>', methods = ['GET'])
def get_by_id(id):
    tutor = Tutors.query.filter_by(id=id).first()
    
    return jsonify(tutor.serialize())


@api.route('/tutors', methods = ['POST'])
def post():
    name = request.json.get('name')
    document_no = request.json.get('document_no')
    
    if not name or not document_no:
        raise InvalidUsage('Invalid request', status_code=400)
    
    try:
        tutor = Tutors(name=name, document_no=document_no)
 
        db.session.add(tutor)
        db.session.commit()
     
        return jsonify({'message': 'Tutor successfully added'})
    except IntegrityError:
        db.session.rollback()
        raise InvalidUsage('Document number already recorded', status_code=409)


@api.route('/tutors/<id>', methods = ['DELETE'])
def delete(id):
    tutor = Tutors.query.filter_by(id=id).first()
    
    if tutor:
        db.session.delete(tutor)
        db.session.commit()
             
        return jsonify({'message': 'Tutor successfully deleted'})
    
    raise InvalidUsage('Tutor not found', status_code=404)


@api.route('/tutors/<id>', methods = ['PUT'])
def put(id):
    tutor = Tutors.query.filter_by(id=id).first()
    
    if tutor:
        name = request.json.get('name')
        document_no = request.json.get('document_no')
        
        if name or document_no:
            try:
                tutor.name = name if name else tutor.name
                tutor.document_no = document_no if document_no else tutor.document_no
            
                db.session.commit()
             
                return jsonify({'message': 'Tutor successfully edited'})
            except IntegrityError:
                db.session.rollback()
                raise InvalidUsage('Document number already recorded', status_code=409)
        else:
            raise InvalidUsage('Invalid request', status_code=400)
    
    raise InvalidUsage('Tutor not found', status_code=404)
