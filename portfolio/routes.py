from flask import Blueprint, request, jsonify
import logging
from portfolio.service import messageService
from portfolio.validations import MessageSchema

bp = Blueprint('message_bp', __name__, url_prefix='/message')
message_schema = MessageSchema()
@bp.route('/', methods=['POST'])
def add():
    errors = message_schema.validate(request.form)
    if errors:
        logging.error(errors)
        return jsonify(message = "Invalid data."), 400 
    data = {}
    data["name"] = request.form["name"]
    data["email"] = request.form["email"]
    data["subject"] = request.form["subject"]
    data["message"] = request.form["message"]
    success, message = messageService.create(data)
    if success:
        logging.info("Successfully saved the message.")
    else:
        logging.info("Failed to save the message.")
    return jsonify(message = message), 201 if success else 400 

@bp.route('/', defaults={'name': None})
@bp.route('/<name>', methods=['GET'])
def get(name):
    logging.info(f"Fetching the records with name({name}).")
    return jsonify(messageService.findAll() if name is None else messageService.findByName(name)), 200

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    rec = messageService.findById(id)
    if rec is None:
        logging.info(f"Record not found with id({id}).")
        return '', 204
    logging.info(f"Deleting the records with id({id}).")
    return jsonify(messageService.delete(id)), 200