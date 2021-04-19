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
    source = get_sources()
    print(source)

    title = 'Home , some of the news sources'
    return render_template('index.html',title=title , source=source)



@main.route('/news')
def news():
    '''
    view news page that returns news detail and its data
    '''
    article=get_article()
  
    return render_template('news.html', article=article, title=title)

@main.route('/search/<article_name>')
def search_article(article_name):
    '''
    View function to display the search results
    '''
    search_article_list = article_name.split(" ")
    search_article_format = "+".join(search_name_list)
    searched_article = search_article(search_name_format)
    title = f'search results for {search_name}'
    return render_template('search.html', articles = searched_movies)


    
  