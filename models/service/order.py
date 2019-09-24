from mongoengine import StringField, IntField, ListField, EmbeddedDocumentField
from mongoengine import Document, EmbeddedDocument


class Order_Model(EmbeddedDocument):
    name = StringField()

    price = IntField()


class Orderlist_Model(Document):
    order_num = IntField()

    customer_name = StringField()

    

    order = ListField(
        EmbeddedDocumentField(Order_Model)
    )