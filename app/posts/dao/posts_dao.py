import json


class PostsDAO:

    def __init__(self, path):
        self.path = path

    def get_all(self) -> list[dict]:
        """
        Load data from json file
        :return: list of all posts
        """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_by_user(self, user_name) -> list[dict]:
        """
        :return: list of posts with 'user_name'
        """
        posts = self.get_all()
        user_posts = []
        for post in posts:
            if user_name == post['poster_name']:
                user_posts.append(post)
        return user_posts

    def search_for_posts(self, query) -> list[dict]:
        """
        :return: list of posts, sorted by query
        """
        posts = self.get_all()
        posts_by_query = []
        for post in posts:
            if query.lower() in post['content'].lower():
                posts_by_query.append(post)
        return posts_by_query

    def get_by_pk(self, post_id) -> dict:
        """
        :return: post by pk
        """
        posts = self.get_all()
        for post in posts:
            if post['pk'] == post_id:
                return post


    # TODO: get_comments_by_post_id(post_id)