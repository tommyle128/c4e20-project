from models.novel import Novel, Chapter
import mlab

mlab.connect()

new_chap = Chapter(
    name = "Persona 5 chap 1",
    content = "Joker",
)
new_chap.save()

new_novel = Novel(
    name = 'Persona 5',
    author = 'Katsuki',
    illu = 'game',
    tag = ['action','mystery'],
    introduce = 'abc',
    chapters = []
)

new_novel.save()    
new_novel.update(push__chapters = new_chap)

