import logging
from flask import request
from flask_restful import Resource
from portfolio.service import messageService
from portfolio.validations import MessageSchema

message_schema = MessageSchema()

class Messages(Resource):
    def get(self):
        if request.args:
            return messageService.filter(request.args.to_dict())
        else:
            return messageService.findAll()

    def post(self):
        errors = message_schema.validate(request.form)
        if errors:
            logging.error(errors)
            return dict(message="Invalid data."), 400
        data = request.form.to_dict()
        success, message = messageService.create(data)
        if success:
            logging.info("Successfully saved the message.")
        else:
            logging.info("Failed to save the message.")
        return dict(message=message), 201 if success else 400


class Message(Resource):
    def get(self, id):
        return messageService.findById(id)

    def delete(self, id):
        rec = messageService.findById(id)
        if rec is None:
            logging.info(f"Record not found with id({id}).")
            return '', 204
        logging.info(f"Deleting the records with id({id}).")
        return {"message": messageService.delete(id)}
