from marshmallow import Schema, fields

#Marshmallow를 사용하여 책 정보를 위한 스키마를 정의합니다.
#책은 최소한 'title'(제목)과 'author'(저자) 필드를 가져야 합니다.

class BookSchema(Schema):
    title = fields.String(required=True)
    author = fields.String(required=True)