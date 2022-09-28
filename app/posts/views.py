from flask import Blueprint, render_template, request
from .dao.posts_dao import PostsDAO


posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO('./data/posts.json')


@posts_blueprint.route('/')
def main_page():
    posts: list[dict] = posts_dao.get_all()
    return render_template('index.html', title='Main page', posts=posts)


@posts_blueprint.route('/users/<user_name>', methods=['GET'])
def get_posts_by_user(user_name):
    posts: list[dict] = posts_dao.get_by_user(user_name)
    return render_template('user-feed.html', title=user_name, posts=posts)


@posts_blueprint.route('/search/')
def get_posts_by_query():
    query = request.args.get('s')
    posts_with_query: list[dict] = posts_dao.search_for_posts(query)
    return render_template('search.html', title=query, posts_with_query=posts_with_query)


@posts_blueprint.route('/posts/<int:post_id>', methods=['GET'])
def get_post_by_post_id(post_id):
    post = posts_dao.get_by_pk(post_id)
    # comments = get_comments_by_post_id(post_id)
    # comments_count = len(comments)
    return render_template('post.html', title=post_id, post=post)