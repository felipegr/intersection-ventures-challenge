# -*- coding: utf-8 -*-

from app import db
from models.tutors import Tutors

from flask import Blueprint, flash, redirect, render_template, request, url_for
from sqlalchemy.exc import IntegrityError

root = Blueprint('root', __name__)


@root.route('/')
def show_all():
    return render_template('show_all.html', tutors = Tutors.query.all())


@root.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['document']:
            flash('Please enter all the fields', 'error')
        else:
            try:
                tutor = Tutors(name=request.form['name'],
                               document_no=request.form['document'])
         
                db.session.add(tutor)
                db.session.commit()
             
                flash('Record was successfully added')
                return redirect(url_for('root.show_all'))
            except IntegrityError:
                flash('Document number already exists in database')
                db.session.rollback()
    
    return render_template('new.html')


@root.route('/delete/<id>', methods = ['GET'])
def delete(id):
    tutor = Tutors.query.filter_by(id=id).first()
    
    if tutor:
        db.session.delete(tutor)
        db.session.commit()
             
        flash('Record was successfully deleted')
    
    return redirect(url_for('root.show_all'))
