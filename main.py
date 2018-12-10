from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    user={'username': 'Jesse'}
    return'''
<html>
    <head>
        <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
</html>'''

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello {}</h1>'.format(name)
