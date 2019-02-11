from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/charsheet/<int:id>', methods = ['GET'])
def charsheet(id):
    return render_template('charsheet.html', id = id)


@app.route('/config')
def config():
    return render_template('config.html')