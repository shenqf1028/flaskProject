from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'name': 'shen',
        'gender': 'male',
        'age': '43'
    },
    {
        'name': 'gu',
        'gender': 'female',
        'age': '43'
    }
]


@app.route('/')
def hello_world():
    return render_template('top.html', posts=posts)


@app.route('/hello')
def hello():
    return render_template('footage.html')


if __name__ == '__main__':
    app.run()
