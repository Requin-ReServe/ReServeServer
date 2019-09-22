from mongoengine import StringField, IntField
from mongoengine import Document


class Market_Model(Document):

    name = StringField()

    location = StringField(primary_key=True)

    telephone_num = StringField()

    authid = IntField()