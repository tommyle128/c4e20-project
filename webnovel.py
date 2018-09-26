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

@app.route('/log_in', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('log_in.html')
    elif request.method == 'POST':
        form = request.form 
        username = form['username']
        password = form['password']

        found_user = User.objects(
            username=username,
            password=password
        )
        if found_user:
            session['loggedin'] = True
            user = User.objects.get(username=username)
            session['user'] = str(user.id)
            return redirect(url_for('homepage.html'))
        else:
            return redirect(url_for('sign_up.html'))

@app.route('/logout')
def logout():
    session['loggedin'] = False
    session.clear()
    return redirect(url_for('index'))

@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html')
    elif request.method == 'POST':
        form = request.form
        fullname = form['fullname']
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
 








































































