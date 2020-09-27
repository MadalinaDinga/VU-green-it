from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    webpage = request.args.get('webpage')
    return render_template("./index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9191)