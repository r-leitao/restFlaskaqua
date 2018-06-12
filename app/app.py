from flask import Flask, render_template
from mocks import Post

app = Flask(__name__)


#creation de fonction handler manuel
# le nom utility_processor peut etre n'importe quoi
@app.context_processor
def utility_processor():
    def pluralize(count, singular, plural=None):
        if not isinstance(count, int):
            raise ValueError('{} must be an integer'.format(count))

        if plural is None:
            plural = singular + 's'

        if plural == 1:
            string = singular
        else:
            string =  plural
        return "{} {}".format(count, string)
    return dict(pluralize=pluralize)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')


@app.route('/blog')
def posts_index():
    return render_template('posts/index.html', posts=Post.all())



@app.route('/blog/posts/<int:id>')
def posts_show(id):
    post = Post.find(id)
    return render_template('posts/show.html', post=post)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
