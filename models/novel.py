from mongoengine import *
from chapter import Chapter

class Novel(Document):
    name = StringField()
    author = StringField()
    illu = StringField()
    tag = ListField()
    introduce = StringField()
    chapters = ListField(ReferenceField(Chapter))
    
