from flask import Flask, request
from flask.views import MethodView




from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/input/<int:number>')
def return_number(number):
    if number == 1:
        return jsonify({'success': True, 'result': 3})
    else:
        return jsonify({'success': False, 'error': 'Invalid input'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
