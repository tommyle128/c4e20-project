from mongoengine import *
from wtforms import Form, StringField, SelectField
 
class NovelSearchForm(Form):
    choices = [('name', 'name'),
               ('author', 'author'),
               ('tag', 'tag')]
    select = SelectField('Search for novel:', choices=choices)
    search = StringField('')

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

class User(Document):
    username = StringField()
    password = StringField()
    email = EmailField()
    
