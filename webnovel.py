from flask import *
import mlab
from mongoengine import *
from models.novel import Novel, Chapter

app = Flask(__name__)
mlab.connect()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/novel')
def novel():
    all_novel = Novel.objects()
    return render_template('novel.html', all_novel = all_novel)

@app.route('/chapter')
def chapter():
    all_chapter = Chapter.objects()
    return render_template('chapter.html', all_chapter = all_chapter)

if __name__ == '__main__':
  app.run(debug=True)
 