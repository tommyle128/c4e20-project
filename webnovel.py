from flask import *
import mlab
from mongoengine import *
from models.chapter import Chapter

app = Flask(__name__)
mlab.connect()

@app.route('/')
def homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
  app.run(debug=True)
 