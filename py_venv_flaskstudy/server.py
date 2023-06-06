from flask import Flask
import random

topics=[
    {'id':1,'title':'python', 'body':'mid'},
    {'id':2,'title':'java', 'body':'deep'},
    {'id':3,'title':'tomcat', 'body':'?'},
    {'id':4,'title':'flask', 'body':'mid'},
    {'id':5,'title':'jenkins', 'body':'mid'},
    {'id':6,'title':'spring.boot', 'body':'?'}
]

def template(contents, content):
    return f'''<!doctype=html>
    <html>
        <title> </title>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>'''

def toptagmake():
    litags=''
    for topic in topics:
        litags=litags+ f"<li><a href='/read/{topic['id']}/'>{topic['title']}</a></li>"
    return litags

app = Flask(__name__)

@app.route('/')
def index():
    return template(toptagmake(),'<h2>Main Page</h2>welcome, Mr.')
        
@app.route('/read/<int:id>/')
def read(id):
    title=''
    body=''
    for topic in topics:
        if id == topic['id']:
            title=topic['title']
            body=topic['body']
            break
    return template(toptagmake(),f'<h2>{title}</h2>{body}')

app.run(port=5001, debug = True)