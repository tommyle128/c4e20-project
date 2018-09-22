from mongoengine import *

class Chapter(Document):
    name = StringField()
    content = StringField()