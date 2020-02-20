from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>', methods=['GET', 'POST'])
def route(title):
    return render_template('base.html', title=title)


if '__main__' == __name__:
    app.run(port=8080, host='127.0.0.1')
