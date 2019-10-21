import datetime
from chalice import Chalice
from chalice import BadRequestError

app = Chalice(app_name='python-chalice-helloworld')
app.debug = True
now = datetime.datetime.now()
CITIES_TO_STATE = {
    'seattle': 'WA',
    'portland': 'OR'
}


@app.route('/')
def index():
    return {'Hello, today is ': now.strftime("%Y-%m-%d %H:%M:%S")}


@app.route('/cities/{city}')
def state_of_city(city):
    try:
        return {'state': CITIES_TO_STATE[city]}
    except KeyError:
        raise BadRequestError("Unknown city '%s', valid choices are: %s" % (city, ', '.join(CITIES_TO_STATE.keys())))


@app.route('/artists/{name}', methods=['PUT'])
def put_artists(name):
    return {"name": name}
