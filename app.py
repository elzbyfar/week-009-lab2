from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xf6U\xb5\xfb\x0c\x17\xca\xd0\xb7|\xe6S\xe0\xa7\xfb\xce \xcd\xd9\xc7#K\xb0Y'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/page_info')
def page_info():
    page_info = request.url
    return render_template('page_info.html', page_info=page_info)

if __name__ == '__main__':
    app.run(debug=True)