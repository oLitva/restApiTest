from flask import Flask, request, jsonify

app = Flask(__name__)

tutorials = [
    {
        'title': 'Video #1 Intro',
        'description': 'GET, POST routes'
    },
    {
        'title': 'Vissdeo #2 More features',
        'description': 'PUT, DELETE routes'
    }
]

@app.route('/tutorials', methods=['GET'])
def get_list():
    return jsonify(tutorials)

if __name__ == '__main__':
    app.run()