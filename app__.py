from flask import Flask, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True
#first endpoint or route in flask
# @app.route('/') #http://www.mysite.com/blog
# def home():
#     return jsonify({'message': 'Hello, world!'})

from flask import render_template
@app.route('/')
def index(): #from flask import render_template
    msg = jsonify({'message': 'Hello, world!'})
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
