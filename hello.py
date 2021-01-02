from flask import Flask, request, render_template
from main import create_grades_table
app = Flask(__name__)


@app.route('/')
def form():
    return render_template('homepage.html.jinja2')


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        title = request.form["Title"]
        grades_table, series_title = create_grades_table(title)
        return render_template('index.html.jinja2', title=series_title, table=grades_table)
