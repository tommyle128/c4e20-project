from flask import *
import mlab
from mongoengine import *
from models.novel import Novel, Chapter
from searchform import NovelSearchForm

app = Flask(__name__)
app.secret_key = "a super hyper bust"
mlab.connect()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/novels')
def novels():
    all_novels = Novel.objects()
    return render_template('novels.html', all_novels=all_novels)

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

       
    
    

@app.route('/log_in', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('log_in.html')
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
        if found_user:
            session['loggedin'] = True
            user = User.objects.get(username=username)
            session['user'] = str(user.id)
            return redirect(url_for('homepage.html'))
        else:
            return redirect(url_for('signup.html'))

@app.route('/logout')
def logout():
    session['loggedin'] = False
    session.clear()
    return redirect(url_for('index'))

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


    
    
    
        


if __name__ == '__main__':
  app.run(debug=True)
 








































































