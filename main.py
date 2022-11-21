from flask import Flask, request, render_template, Blueprint
from utils import *
import logging
from api.api import api_bp

app = Flask(__name__)

logging.basicConfig(filename="./logs/api.log")
formatter = logging.Formatter("%(asctime)s : [%(levelname)s] : %(message)s")


@app.route('/')
def index_page():

    posts = get_posts_all()

    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def post_page(postid):

    post_by_id = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    comments_counter = len(comments)
    content = get_tags(post_by_id['content'])

    if not post_by_id:
        return "Такого поста не существует!"

    return render_template('post.html', post=post_by_id, comments=comments, comments_counter=comments_counter, content=content)


@app.route('/search')
def search_page():

    content = request.args.get('s')
    posts_by_search = search_for_posts(content)
    posts_counter = len(posts_by_search)

    return render_template('search.html', posts=posts_by_search, content=content, counter=posts_counter)


@app.route('/users/<username>')
def user_page(username):

    posts_by_user = get_posts_by_user(username)

    if not posts_by_user:
        return "Такого пользователя нет!"

    return render_template('user-feed.html', username=username, posts=posts_by_user)


@app.errorhandler(404)
def page_404(error):

    return "404 NOT FOUND"


@app.errorhandler(500)
def page_500(error):

    return "500 Internal Server Error"


app.register_blueprint(api_bp)


if __name__ == '__main__':
    app.run(debug=True)



