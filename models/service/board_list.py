from mongoengine import StringField, IntField, EmbeddedDocumentField
from mongoengine import Document, EmbeddedDocument


class BoardModel(EmbeddedDocument):
    name = StringField()

    price = IntField()

class Boardlist_Model(Document):
    board_id = IntField()

    auth_id = IntField()

    menu = EmbeddedDocument(BoardModel)