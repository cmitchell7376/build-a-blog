from flask import Flask, redirect, request, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Blog123@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.String(200))

    def __init__(self,title,text):
        self.title = title
        self.text = text

@app.route("/", methods=['POST', 'GET'])
def Main_page():

    blog_entry = Blog.query.all()
    return render_template("blog.html", blog_entry = blog_entry)


@app.route("/entry", methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog_title = request.form['blog_title']
        blog_text = request.form['blog_text']
        blog_entry = Blog(blog_title,blog_text)
        db.session.add(blog_entry)
        db.session.commit()

        return redirect('/')

    return render_template("index.html")








if __name__ == '__main__':
    app.run()