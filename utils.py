import json


def load_json_file(filename):
    """Функция, с помощью которой подгружается файл формата JSON"""

    with open(filename, 'rt', encoding='utf-8') as file:
        json_file = json.load(file)

    return json_file


def get_posts_all():
    """Функция, с помощью которой подгружается список со всеми постами из файла формата JSON"""

    posts_list = load_json_file('./data/posts.json')

    return posts_list


def get_posts_by_user(username):
    """Функция, с помощью которой получаем посты конкретного пользователя по нику (имени)"""

    posts_list = get_posts_all()
    posts_by_user = []
    for post in posts_list:
        if username.lower() in post['poster_name'].lower():
            posts_by_user.append(post)

    return posts_by_user


def get_comments_by_post_id(post_id):
    """Функция, с помощью которой получаем список комментариев к конкретному посту"""

    comments_list = load_json_file('./data/comments.json')
    comments_by_post_id = []
    for comments in comments_list:
        if int(comments['post_id']) == int(post_id):
            comments_by_post_id.append(comments)

    return comments_by_post_id


def search_for_posts(content):
    """Функция, с помощью которой ищем посты по ключевым словам в описании"""

    posts_list = get_posts_all()
    posts_by_content = []
    for post in posts_list:
        if content.lower() in post['content'].lower():
            posts_by_content.append(post)

    return posts_by_content


def get_post_by_pk(pk):
    """Фукнция, с помощью которой получаем конкретный пост по номеру (postid)"""

    posts_list = get_posts_all()
    for post in posts_list:
        if int(post['pk']) == int(pk):
            return post


def wrap_to_link(tag):
    """Функция, с помощью которой преобразуем необходимый хэштег для корректного отображения в HTML шаблоне"""

    return f"<a href='/tags/{tag}'>#{tag}</a>"


def get_tags(content):
    """Функция, с помощью которой получаем слова, которые начинаются на #"""

    words = []
    for word in content.split(" "):
        if word.startswith('#'):
            words.append(wrap_to_link(word[1:]))
        else:
            words.append(word)
    return " ".join(words)
