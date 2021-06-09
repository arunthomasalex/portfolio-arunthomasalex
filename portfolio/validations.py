from marshmallow import (
    Schema,
    fields,
    validate
)

class MessageSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Str(required=True, validate=validate.Email(error="Not a valid email address"))
    subject = fields.Str(required=True)
    message = fields.Str(required=True)