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
   

    
class User(Document):
    username = StringField()
    password = StringField()
    email = EmailField()
    is_admin = BooleanField()

class SearchNovel(Document):
    name =StringField()    
    novels = ListField(ReferenceField(Novel))

class New(Document):
    new_novel = ListField(ReferenceField(Novel))
    new_chapter = ListField(ReferenceField(Chapter))

    
