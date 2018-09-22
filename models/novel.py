from mongoengine import *

class Novel(Document):
    name = StringField()
    author = StringField()
    illu = StringField()
    tag = ListField()
    introduce = StringField()
    chapters = List(ReferenceField(Chapter))
    
