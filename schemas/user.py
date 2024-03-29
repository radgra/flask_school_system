from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    
    class Meta:
        load_only = ('password',)
        dump_only = ('id',)
        # keeps fields in order
        ordered = True