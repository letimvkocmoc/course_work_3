from flask import Blueprint, jsonify
import utils

api_bp = Blueprint('api_bp', __name__, template_folder='./api/templates', url_prefix='/api')


@api_bp.route('/posts/')
def api_posts():

    posts = utils.get_posts_all()
    return jsonify(posts)


@api_bp.route('/posts/<int:postid>')
def api_post(postid):

    post_by_id = utils.get_post_by_pk(postid)
    return jsonify(post_by_id)