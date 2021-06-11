from flask import Blueprint, request, jsonify

# bp = Blueprint('message_bp', __name__, url_prefix='/message')
# message_schema = MessageSchema()
# @bp.route('/', methods=['POST'])
# def add():
#     errors = message_schema.validate(request.form)
#     if errors:
#         logging.error(errors)
#         return jsonify(message = "Invalid data."), 400
#     data = {}
#     data["name"] = request.form["name"]
#     data["email"] = request.form["email"]
#     data["subject"] = request.form["subject"]
#     data["message"] = request.form["message"]
#     success, message = messageService.create(data)
#     if success:
#         logging.info("Successfully saved the message.")
#     else:
#         logging.info("Failed to save the message.")
#     return jsonify(message = message), 201 if success else 400

# @bp.route('/', defaults={'name': None})
# @bp.route('/<name>', methods=['GET'])
# def get(name):
#     logging.info(f"Fetching the records with name({name}).")
#     return jsonify(messageService.findAll() if name is None else messageService.findByName(name)), 200

# @bp.route('/<int:id>', methods=['DELETE'])
# def delete(id):
#     rec = messageService.findById(id)
#     if rec is None:
#         logging.info(f"Record not found with id({id}).")
#         return '', 204
#     logging.info(f"Deleting the records with id({id}).")
#     return jsonify(messageService.delete(id)), 200

bp = Blueprint('routes_bp', __name__)

@bp.route(rule='/', methods=['GET'])
def index():
    from app import app
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({"methods": [method for method in rule.methods if method not in ['HEAD', 'OPTIONS']], "path": rule.rule})
    return jsonify(routes)

def createValidatioRule(obj):
    from marshmallow.validate import Length, Email
    fields = []
    for key, value in obj.fields.items():
        validations = {}
        for validation in value.validate:
            if isinstance(validation, Length):
                validations["length"] = {}
                if validation.min:
                    validations["length"]["min"] = validation.min
                if validation.max:
                    validations["length"]["max"] = validation.max
            elif isinstance(validation, Email):
                validations["email"] = True
        fields.append({key: {"required": value.required, "validations": validations}})
    return fields

@bp.route(rule="/rule/<name>", methods=["GET"])
def validations(name):
    import imp
    try:
        fp, path, desc = imp.find_module(f"portfolio")
        schema_class = imp.load_module(f"portfolio.validations", fp, path, desc)
        return jsonify(createValidatioRule(eval(f"schema_class.{name.capitalize()}Schema()")))
    except Exception as e:
        return jsonify(dict(message=f"Rule for {name} is not defined."))
