#!/usr/bin/python3
<<<<<<< HEAD
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
"""simple flask app
"""
from flask import Flask, render_template
from models import storage
from os import environ as env
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """reload storage after each request
    """
    storage.close()


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def states_cities_list(id=None):
    """show state and cities if id is given
    otherwise list all states
    """
    states = storage.all("State")
    if id:
        state = states.get('State.{}'.format(id))
        states = [state] if state else []
    else:
        states = list(states.values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    return render_template(
        '9-states.html',
        states=states,
        len=len(states),
        id=id
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> d2bcc03fe412038f3218b5eb2721eb73340255d1
