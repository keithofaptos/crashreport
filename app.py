import os
from flask import Flask, abort, request
from werkzeug.utils import secure_filename

app = Flask('crashreport')

@app.route('/<uuid>/upload', methods=['POST'])
@app.route('/crashreport/<uuid>/upload', methods=['POST'])
def upload(uuid):
    if len(request.files.keys()) != 1:
        return abort(400)

    base = os.path.join('upload', secure_filename(uuid))
    if not os.path.exists(base):
        os.makedirs(base)

    f = request.files.values()[0]
    path = os.path.join(base, secure_filename(f.filename))
    if not os.path.exists(path):
        f.save(path)
    return 'ok'

if __name__ == '__main__':
    app.run(port=5000, debug=True, threaded=True)
