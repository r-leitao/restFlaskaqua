from flask import abort
class Post():
    """docstring for Post."""

    POSTS = [
        {'id':1 , 'title':'First', 'content': 'This my first post'},
        {'id':2 , 'title':'Second', 'content': 'This my second post'},
        {'id':3 , 'title':'Third', 'content': 'This my third post'},
    ]

    @classmethod
    def all(cls):
        return cls.POSTS

    @classmethod
    def find(cls, id):
        try:
            return cls.POSTS[id - 1]
        except IndexError:
            abort(404)
