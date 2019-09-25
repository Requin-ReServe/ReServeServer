from mongoengine import StringField, ListField, IntField, EmbeddedDocumentField
from mongoengine import Document, EmbeddedDocument


class BoardModel(EmbeddedDocument):
    name = StringField()

    price = IntField()


class Boardlist_Model(Document):
    board_id = IntField(primary_key=True)

    market_id = IntField()

    menu = ListField(
        list = EmbeddedDocumentField(BoardModel)
    )