from mongoengine import StringField, DictField, ListField ,IntField # ETC....import
from mongoengine import Document, EmbeddedDocumentField, EmbeddedDocument


class Emb(EmbeddedDocument):
    name = StringField()
    count = IntField()


class ExampleCol(Document):
        id = StringField(primary_key=True)

        order = ListField(
            EmbeddedDocumentField(Emb)
        )