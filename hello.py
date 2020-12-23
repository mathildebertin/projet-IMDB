from flask import Flask, render_template
from main import create_grades_table
app = Flask(__name__)

title = "The Big Bang Theory"

@app.route('/', methods = ['GET'])
def index():
    grades_table = create_grades_table(title)
    return render_template('index.html.jinja2', title=title, table = grades_table)


@app.route('/<int:post_id>', methods = ['POST'])
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/toto')
def toto():
    return "toto"