from flask import Flask, redirect, request, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Blog123@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blogs_title = db.Column(db.String(120))
    entry = db.Column(db.String(200))

    def __init__(self,blogs_title,entry):
        self.blogs_title = blogs_title
        self.entry = entry

@app.route("/entry", methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        blog_name = request.form['blog_title']
        blog_text = request.form['blog_text']
        blog_entry = Blog(blog_name,blog_text)
        db.session.add(blog_entry)
        db.session.commit()

    return render_template("index.html",title="Blog")








if __name__ == '__main__':
    app.run()