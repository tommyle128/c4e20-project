from wtforms import Form, StringField, SelectField
 
class NovelSearchForm(Form):
    choices = [('name', 'name'),
               ('author', 'author'),
               ('tag', 'tag')]
    select = SelectField('Search for novel:', choices=choices)
    search = StringField('')