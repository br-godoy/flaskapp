from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/home', methods=['GET', 'POST'], defaults={'name': 'default'})
@app.route('/home/<string:name>', methods=['GET', 'POST'])
def home(name: str):
    return '<h1>Hi, {}. You are on the homepage</h1>'.format(name.title())

@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1,2,3,4]})

@app.route('/query')
def query():
    name: str = request.args.get('name')
    location: str = request.args.get('location')
    return '<h1>Hi {}! You are from {} and you are on the query page.</h1>'.format(name.title(), location.title())

@app.route('/theform', methods=['GET', 'POST'])
def theform():
    if request.method == 'GET':
        return '''
            <form method="POST" action="/theform">
                <input type="text" name="name" placeholder="Name">
                <br>
                <input type="text" name="location" placeholder="Location">
                <br>
                <input type="submit" value="Submit">
            </form>
        '''
    else:
        name: str = request.form.get('name')
        location: str = request.form.get('location')
        return '<h1>Hi {}. You are from {}. You subimitted the form successfully!</h1>'.format(name.title(), location.title())
    
@app.route('/processjson', methods=['POST'])
def processjson():
    data: dict = request.get_json()
    name = data.get('name')
    location = data.get('location')
    random_list = data.get('randomList')
    return jsonify({'status': 200,'result': "Success", "name": name, "location": location, "randomItem": random_list[1], "data": data})

if __name__ == '__main__':
    app.run(debug=True)