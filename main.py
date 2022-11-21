from flask import Flask, request, render_template, Blueprint
from utils import *
import logging
from api.api import api_bp

app = Flask(__name__)

# подключаем стандартное логирование
logging.basicConfig(filename="./logs/api.log")
formatter = logging.Formatter("%(asctime)s : [%(levelname)s] : %(message)s")


@app.route('/')
def index_page():
    """Главная страница со списком всех постов"""

    posts = get_posts_all()

    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def post_page(postid):
    """Страница с конкретным постом по <postid>"""

    # получаем конкретным пост по id
    post_by_id = get_post_by_pk(postid)
    # получаем комментарии к необходимому посту
    comments = get_comments_by_post_id(postid)
    # счетчик комметариев
    comments_counter = len(comments)
    # узнаем, есть ли в описании поста хэштеги и преобразуем текст для корректного отображения хэштегов
    content = get_tags(post_by_id['content'])

    # если запрос с несуществующим id выдаст информацию об отсутствии такового
    if not post_by_id:
        return "Такого поста не существует!"

    return render_template('post.html', post=post_by_id, comments=comments, comments_counter=comments_counter, content=content)


@app.route('/search')
def search_page():
    """Поиск по ключевым словам в описании к постам"""

    # получаем запрос от пользователя
    content = request.args.get('s')
    # ищем посты с указанным запросом
    posts_by_search = search_for_posts(content)
    # считаем количество найденных постов
    posts_counter = len(posts_by_search)

    return render_template('search.html', posts=posts_by_search, content=content, counter=posts_counter)


@app.route('/users/<username>')
def user_page(username):
    """Страница с постами конкретного юзера"""

    # получаем посты конкретного юзера по его нику (имени)
    posts_by_user = get_posts_by_user(username)

    # если пользователя с таким ником (именем) нет, выдаст информацию об отсутствии такового
    if not posts_by_user:
        return "Такого пользователя нет!"

    return render_template('user-feed.html', username=username, posts=posts_by_user)


@app.errorhandler(404)
def page_404(error):
    """Страница с ошибкой, если пользователь запросил несуществующую страницу"""

    return "404 NOT FOUND"


@app.errorhandler(500)
def page_500(error):
    """Страница с ошибкой, если произошла ошибка на сервере"""

    return "500 Internal Server Error"


# регистрируем блупринт
app.register_blueprint(api_bp)


if __name__ == '__main__':
    app.run(debug=True)



