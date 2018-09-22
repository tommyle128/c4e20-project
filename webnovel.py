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

@app.route('/test/', methods=["GET", "POST"])
def test():
    if request.method == "GET":
        return render_template ('test.html')
    elif request.method == "POST":
        test_form = request.form
        name = test_form['name']
        content = test_form['editor1']
                
        new_chapter = Chapter(
            name=name,
            content=content,
        )
        new_chapter.save()

        return redirect(url_for('homepage'))

if __name__ == '__main__':
  app.run(debug=True)
 