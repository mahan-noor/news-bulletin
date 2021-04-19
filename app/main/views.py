from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources,get_article
from .models import source




# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    Genaral_news
    return render_template('index.html',message = message)