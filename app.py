from flask import Flask
from flask import render_template
from data import title, subtitle, description, departures, tours

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title=title, tours=tours, departures=departures)


@app.route('/departures/<departure>/')
def dep(departure):
    return render_template('departure.html', title=title, tours=tours, departures=departures, departure=departure)


@app.route('/tours/<int:id>/')
def tour(id):
    return render_template('tour.html', title=title, tours=tours, departures=departures, id=id)


if __name__ == '__main__':
    app.run(debug=True)



