from flask import *
import mlab
from mongoengine import *
from models.novel import Novel, Chapter, User
from models.search import NovelSearchForm

app = Flask(__name__)
app.secret_key = 'a super super secret key'
mlab.connect()



@app.route('/')
def homepage():
    all_novels = Novel.objects()
    return render_template('homepage.html', all_novels=all_novels)

@app.route('/chapters/<novel_id>')
def chapters(novel_id):
    novel = Novel.objects.with_id(novel_id)
    all_chapters = novel['chapters']
       
    return render_template('chapters.html', all_chapters=all_chapters, novel_id=novel_id)
    
@app.route('/content/<novel_id>/<chapter_id>')
def content(chapter_id, novel_id):
    chapter = Chapter.objects.with_id(chapter_id)
    
    novel = Novel.objects.with_id(novel_id)
    all_chapters = novel['chapters']

    for i in range(len(all_chapters)):
        if str(all_chapters[i].id) == chapter_id:
            order_number = i
            if order_number == 0:
                chapter_id_previous = "None"
                if len(all_chapters) == 1:
                    chapter_id_next = "None"
                else:
                    chapter_id_next = str(all_chapters[i+1].id)
        
            elif order_number == len(all_chapters)-1:
                chapter_id_next = "None"
                chapter_id_previous = str(all_chapters[i-1].id)
            
            else:
                chapter_id_next = str(all_chapters[i+1].id)
                chapter_id_previous = str(all_chapters[i-1].id)
    
    return render_template('content.html', 
        chapter=chapter, 
        chapter_id_next=chapter_id_next, 
        chapter_id_previous=chapter_id_previous,
        novel_id=novel_id)

       
    
    

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

        if username == "":
            return "Hãy điền tên đăng nhập"
        else:
            if password == "":
                return "Hãy nhập mật khẩu"
            else:
                found_user = User.objects(
                    username=username,
                    password=password,
                )
                if len(found_user) > 0:
                    session['loggedin'] = True
                    user_id = found_user[0].id
                    user_name = found_user[0].username
                    all_novels = Novel.objects()
                    if found_user[0].is_admin == True:
                        return render_template('admin/homepage.html',all_novels=all_novels)
                    else:
                        return render_template('user/homepage.html',all_novels=all_novels,user_id=user_id,user_name=user_name)
                else:
                    return redirect(url_for('signup'))

@app.route('/user/<user_id>')
def user(user_id):
    user = User.objects.with_id(user_id)
    all_novel = user['novels'] 
    return render_template('user.html',user=user,user_id=user_id,all_novel=all_novel)

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

@app.route('/admin')
def admin():
    return render_template('admin.html')

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



@app.route('/user_homepage')
def user_homepage():
    return render_template('user/homepage.html')


@app.route('/upload-novel/')
def upload_novel():
    all_novels = Novel.objects()
    return render_template('upload-novel.html', all_novels=all_novels)

@app.route('/new-novel/', methods=["GET", "POST"])
def new_novel():
    if request.method == "GET":
        return render_template('new-novel.html')
    elif request.method == "POST":
        test_form = request.form
        return "OK"
    

@app.route('/new-chapter', methods=["GET", "POST"])
def upload_chapter():
    if request.method == "GET":
        return render_template('new-chapter.html')
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

@app.route('/delete/<user_id>/<novel_id>')
def delete(user_id,novel_id):
    user = User.objects.with_id(user_id)
    novel_to_delete = Novel.objects.with_id(novel_id)
    all_novel = user['novels']
    User.objects(id = user_id).update_one(pull__novels = novel_to_delete)
    if novel_to_delete is not None:
        novel_to_delete.delete()
        user = User.objects.with_id(user_id)
        all_novel = user['novels']
        return render_template('user.html',user=user,user_id=user_id,all_novel=all_novel,novel_id=novel_id)
    else:
        return 'Novel not found'

        


if __name__ == '__main__':
  app.run(debug=True)
 








































































