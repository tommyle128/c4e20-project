from flask import *
import mlab
from mongoengine import *
from models.novel import Novel, Chapter, User

app = Flask(__name__)
app.secret_key = 'a super super secret key'
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

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form 
        username = form['username']
        password = form['password']

@app.route('/signup', methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST":
        found_user = User.objects(
            username=username,
            password=password
        )

        if username == "":
            return "Hãy điền tên đăng nhập"
        else:
            if password == "":
                return "Hãy nhập mật khẩu"
            else:
                if found_user:
                    session['loggedin'] = True
                    user = User.objects.get(username=username)
                    session['user'] = str(user.id)
                    return redirect(url_for('homepage'))
                else:
                    return redirect(url_for('signup'))

@app.route('/logout')
def logout():
    session['loggedin'] = False
    session.clear()
    return redirect(url_for('homepage.html'))

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        form = request.form
        email = form['email']
        username = form['username']
        password = form['password']

        new_user = User(
            email=email,
            username=username,
            password=password,
        )

        if email == "":
            return "Hãy điền email của bạn"
        else:
            if username == "":
                return "Hãy điền tên đăng nhập của bạn"
            else:
                if password == "":
                    return "Hãy điền mật khẩu của bạn"
                else:
                    found_user = User.objects(
                        email=email,
                        username=username,
                    )
                    if found_user:
                        return "Tài khoản đã tồn tại!"
                    else:
                        new_user.save()
                        return "Đã đăng kí thành công!"

@app.route('/search', methods=['GET', 'POST'])
def search():
    search = NovelSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('search.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search.data['search'] == '':
        qry = db_session.query(Album)
        results = qry.all()
 
    if not results:
        flash('No results found!')
        return redirect('/search')
    else:
        return render_template('results.html', results=results)

if __name__ == '__main__':
  app.run(debug=True)
 








































































