from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_articles

from ..models import News


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    sports_news = get_news()
    title = "News App - Where news live on"
    return render_template('index.html' , title = title, sports_news = sports_news)  

@main.route('/articles')
def articles():
	'''
	view articles page
	'''
	articles = get_articles('articles')


	title = 'articles'
    

	return render_template('articles.html',title= title,articles = articles)
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


    
  