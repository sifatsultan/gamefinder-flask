__author__ = 'Sifat'
import flask, os, werkzeug
import json

FOLDER = 'files/'
app = flask.Flask(__name__)


@app.route('/')
def upload_form():
    html = open('upload_form.html').read()
    return html


# read json and display details of game in browser
@app.route('/sort', methods=['POST'])
def sort_games():
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

    file = flask.request.files['the_file']

    filename = werkzeug.secure_filename(file.filename)
    file.save(FOLDER+filename)

    f = open(filename, 'r')
    data = json.load(f)

    try:
        if data:
            html = '<ul>'
            for game in data:
                html += '<li>'+game+'</li>\n'
            html += '</ul>'
        return html
    except:
        return 'Some unknown exception, could not return html!'

@app.route('/'+FOLDER+'<filename>')
def view_file(filename):
    return flask.send_from_directory(FOLDER, filename)

if __name__=='__main__':
    app.run()

