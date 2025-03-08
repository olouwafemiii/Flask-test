from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=False)
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))
    created_at = fields.DateTime(dump_only=True)
