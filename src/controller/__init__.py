from flask import Blueprint, jsonify

controller_index = Blueprint('controller_index', __name__)

@controller_index.route('/')
def index():
    return jsonify(dict(
        name='API Sicon',
        version='Alpha 1.0',
        author=[dict(
            name='Felipe Toffoli Martins',
            linkedin='https://www.linkedin.com/in/felipetoffoli',
            github='https://github.com/felipetoffoli'
        ),
        dict(
            name='Guilherme Holanda Saravi',
            linkedin='https://www.linkedin.com/in/guilhermesaravi/',
            github='https://github.com/GuilhermeSaravy'
        )],
        repository='https://github.com/machine-projects/SICON_API'
        ))