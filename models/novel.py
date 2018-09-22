from mongoengine import *

class Chapter(Document):
    name = StringField()
    content = StringField()

class Novel(Document):
    name = StringField()
    author = StringField()
    illu = StringField()
    tag = ListField()
    introduce = StringField()
    chapters = ListField(ReferenceField(Chapter))
    
