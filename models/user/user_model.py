from mongoengine import StringField, IntField
from mongoengine import Document


class User_Model(Document):
    id = StringField(primary_key=True)

    name = StringField()

    pw = StringField()

    point = IntField()

    user_type = IntField()

    phone_num = StringField()