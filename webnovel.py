from flask import *
import mlab
from mongoengine import *
from models.chapter import Chapter

app = Flask(__name__)
mlab.connect()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/novel')
def novel():
    return render_template('novel.html')

if __name__ == '__main__':
  app.run(debug=True)
 