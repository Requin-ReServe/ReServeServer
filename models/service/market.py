from mongoengine import StringField, IntField, ListField
from mongoengine import Document, EmbeddedDocumentField, EmbeddedDocument

class BoardModel(EmbeddedDocument):
    name = StringField()

    price = IntField()

    description = StringField


class Market_Model(Document):

    owner_id = StringField()

    name = StringField()

    location = StringField()

    telephone_num = StringField()

    market_id = IntField(primary_key=True)

    image = StringField()

    menu = ListField(
        list = EmbeddedDocumentField(BoardModel)
    )

    meta = {
            'indexes': [
                {
                    'fields': [
                        '$name', '$location'
                    ],
                    'weights': {
                        'name': 6, 'location': 10
                    }
                }
        ]
    }
