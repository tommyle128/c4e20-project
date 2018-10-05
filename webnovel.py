from flask import *
import mlab
from mongoengine import *
from models.novel import Novel, Chapter, User, SearchNovel


app = Flask(__name__)
app.secret_key = 'a super super secret key'
mlab.connect()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/<novel>')
def novel(novel):
    all_novel = Novel.objects()
    return render_template('novel.html', all_novel = all_novel)

@app.route('/chapter')
def chapter():
    all_chapter = Chapter.objects()
    return render_template('chapter.html', all_chapter = all_chapter)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

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
                if len(found_user) > 0:
                    session['loggedin'] = True
                    if found_user[0].is_admin == True:
                        return redirect(url_for('admin'))
                    else:
                        return redirect(url_for('homepage'))
                else:
                    return redirect(url_for('signup'))

@app.route('/logout')
def logout():
    session['loggedin'] = False
    session.clear()
    return redirect(url_for('homepage'))

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
    if request.method == 'GET':
        return render_template('search.html')
    elif request.method == 'POST':
        form = request.form
        search_querry = form['name']
        
        all_novels = Novel.objects()
        for i in range(len(all_novels)):
            
            if search_querry.lower() in all_novels[i]['name'].lower():
                result_name = all_novels[i]['name']
                result_link = all
            # else:
            #     return "Not found"

@app.route('/results')
def search_results(search):
    search_string = search.data['search']
    NovelList = Novel.objects()
    for i in range(len(NovelList)):
        if search_string == Novel.objects(name = search_string):
            return "yes"
        
    
        # if not results:
        #     flash('No results found!')
        #     return redirect('/search')
        # else:
        #     return render_template('results.html', results=results)

if __name__ == '__main__':
  app.run(debug=True)
 








































































