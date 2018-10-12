from mongoengine import *

class Chapter(Document):
    name = StringField()
    content = StringField()

class Novel(Document):
    name = StringField()
    author = StringField()
    tag = ListField()
    introduce = StringField()
    chapters = ListField(ReferenceField(Chapter))
    avatar_img = URLField()
    bg_img = URLField()

    
class User(Document):
    username = StringField()
    password = StringField()
    email = EmailField()
    is_admin = BooleanField()
    novels = ListField(ReferenceField(Novel))

class New(Document):
    new_novel = ListField(ReferenceField(Novel))
    new_chapter = ListField(ReferenceField(Chapter))

    
