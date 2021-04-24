from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('base.html', name=name)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)