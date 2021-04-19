from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources,get_article
from .models import source,article




# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    
  