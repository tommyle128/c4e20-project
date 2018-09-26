from flask import *
import mlab
from mongoengine import *
from models.novel import Novel, Chapter

app = Flask(__name__)
mlab.connect()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/<novel>')
def novel(novel):
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

        return redirect(url_for('login'))

@app.route('/signup', methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        email = form['email']
        username = form['username']
        password = form['password']

        signin = Signin(
            name=name,
            email=email,
            username= username,
            password=password,
        )
    if email != "" and name != "":
        signin.save()
        return "Saved"
    else:
        if email == "" and name != "":
            return "You must fill in your email"
        elif name == "" and email != "":
            return "You must fill in your fullname"
        else:
            return "You must fill in your full name and email"

if __name__ == '__main__':
  app.run(debug=True)
 








































































