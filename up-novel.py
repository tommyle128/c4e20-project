from models.novel import Novel, Chapter, User
import mlab

mlab.connect()

# new_user = User(
#     username = 'man',
#     password = 'man',
#     is_admin = False,
# )
# new_user.save()

new_user = User(
    username = 'woman',
    password = 'woman',
    is_admin = False,
    novels = []
)
new_user.save()

new_novel = Novel(
    name = 'AOT',
    author = 'Katsuki',
    tag = ['action','mystery'],
    introduce = 'abc',
    chapters = []
)
new_novel.save() 
new_user.update(push__novels = new_novel)  

for i in range(5):
    new_chap = Chapter(
        name = 'Persona chap ' + str(i),
        content = "Batman",
    )
    new_chap.save()
    
    new_novel.update(push__chapters = new_chap)



# new_novel = Novel(
#     name = 'Persona 3',
#     author = 'Katsuki',
#     illu = 'game',
#     tag = ['action','mystery'],
#     introduce = 'abc',
#     chapters = []
# )
# new_novel.save()    

# for i in range(2):
#     new_chap = Chapter(
#         name = 'Persona 3 chap ' + str(i),
#         content = "Mona",
#     )
#     new_chap.save()
    
#     new_novel.update(push__chapters = new_chap)

