from marshmallow import (
    Schema,
    fields,
    validate
)

class MessageSchema(Schema):
    name = fields.Str(required=True, validate=[validate.Length(min=1, max=20, error="Name should be between 1 to 20")])
    email = fields.Str(required=True, validate=[validate.Email(error="Not a valid email address"), validate.Length(min=1, max=100, error="Email should be between 1 to 100")])
    subject = fields.Str(required=True, validate=[validate.Length(min=1, max=100, error="Subject should be between 1 to 100")])
    message = fields.Str(required=True, validate=[validate.Length(min=1, max=500, error="Message should be between 1 to 500")])