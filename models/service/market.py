from mongoengine import StringField, IntField
from mongoengine import Document


class Market_Model(Document):

    owner_name = StringField()

    name = StringField()

    location = StringField(primary_key=True)

    telephone_num = StringField()

    authid = IntField()

    meta = {
        'indexes': [
            {
                'fields': [
                    '$name', "$location"
                ],
                'weights': {
                    'name': 8, 'location': 10
                }
            }
    ]
    }
