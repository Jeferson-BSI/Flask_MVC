from flask import abort, Blueprint, render_template, request, redirect, url_for

from favoritesUrl.models import  URL

from favoritesUrl.ext.database import db



main = Blueprint('main', __name__)


def index():
    return render_template("index.html")

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/urls', methods=['GET','POST'])
def urls():

    print(request.method)
    if request.method == 'POST':
        url = request.form.get('url')
        new_url = URL(url=url)
        db.session.add(new_url)
        db.session.commit()
    
    urls = URL.query.all()
    return render_template('urls.html', urls=urls)
