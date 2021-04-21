from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_article,search_article
from ..models import source




# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data

    '''
    sources = get_sources()

    title = 'Home'
    return render_template('index.html',title=title,sources=sources)



@main.route('/article')
def article():
    '''
    View articles page that returns articles detail and its data
    '''
    article = get_article()
  
    return render_template('article.html', article=article,title=title)

@main.route('/search/<article_name>')
def search_article(article_name):
    '''
    View function to display the search results
    '''
    search_article_name = article_name.split(" ")
    search_article_format = "+".join(search_article_name)
    searched_article = search_article(search_name_format)
    title = f'search results for {search_name}'
    return render_template('search.html', articles = searched_)


    
  