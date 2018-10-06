from flask import *
import mlab
from mongoengine import *
from models.novel import Novel, Chapter, User, SearchNovel


app = Flask(__name__)
app.secret_key = 'a super super secret key'
mlab.connect()


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/')
def homepage():
    all_novels = Novel.objects()
    return render_template('homepage.html', all_novels=all_novels)

@app.route('/chapters/<novel_id>')
def chapters(novel_id):
    novel = Novel.objects.with_id(novel_id)
    all_chapters = novel['chapters']
    
    return render_template('chapters.html', all_chapters=all_chapters, novel=novel)
    
@app.route('/content/<novel_id>/<chapter_id>')
def content(chapter_id, novel_id):
    chapter = Chapter.objects.with_id(chapter_id)
    
    novel = Novel.objects.with_id(novel_id)
    all_chapters = novel['chapters']

    for i in range (len(all_chapters)):
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

        found_user = User.objects(
            username=username,
            password=password,
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
                        all_novel = Novel.objects()
                        return render_template('user/homepage.html',all_novel=all_novel)
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
                return render_template('result.html')
            else:
                return "Not found"

@app.route('/result')
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

@app.route('/user/<user_id>')
def user(user_id):
    user = User.objects.with_id(user_id)
    return render_template('user.html',user=user)

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
                
        new_novel = Novel(
            name = test_form['name'],
            author = test_form['author'],
            tag = [test_form['tag1'], test_form['tag2'], test_form['tag3']],
            introduce = test_form['introduce'],
            chapters = []
        )
        new_novel.save()
          
        return redirect(url_for('new_chapter', novel_id=new_novel.id))
    

@app.route('/new-chapter/<novel_id>', methods=["GET", "POST"])
def new_chapter(novel_id):
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

        novel = Novel.objects.with_id(novel_id)
        novel.update(push__chapters = new_chapter)

        return redirect(url_for('upload_novel'))
    

if __name__ == '__main__':
  app.run(debug=True)
 








































































