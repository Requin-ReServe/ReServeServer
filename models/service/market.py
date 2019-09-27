from mongoengine import StringField, IntField
from mongoengine import Document


class Market_Model(Document):

    owner_id = StringField()

    name = StringField()

    location = StringField(primary_key=True)

    telephone_num = StringField()

    market_id = IntField()

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
