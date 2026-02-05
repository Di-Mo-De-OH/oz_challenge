from marshmallow import Schema,fields
    

class BookSchemas(Schema):
    book_id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)