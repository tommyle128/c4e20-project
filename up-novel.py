from models.novel import Novel, Chapter, User
import mlab

mlab.connect()

# new_user = User(
#     username = 'man',
#     password = 'man',
#     is_admin = False,
# )
# new_user.save()
new_novel = Novel(
    name = 'Persona 5',
    author = 'Katsuki',
    tag = ['action','mystery'],
    introduce = 'abc',
    chapters = []
)
new_novel.save()   

# for i in range(2):
#     new_chap = Chapter(
#         name = 'Persona 5 chap ' + str(i),
#         content = "Joker",
#     )
#     new_chap.save()
    
#     new_novel.update(push__chapters = new_chap)

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

