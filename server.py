from bottle import route, run, view, static_file 
from horoscope import generate_prophecies
from datetime import datetime as dt


@route("/")
@view ("prediction")
def index():
	now = dt.now()
	return {"date": f"{now.year}-{now.month}-{now.day}"}


@route("/api/forecasts")
def api_test():
	prophecies = generate_prophecies(6,2)

	return {"prophecies":prophecies}

@route("/scripts.js")
def styles_css():
    return static_file("scripts.js", root="")

run(
	host = "localhost",
	port = 8080,
	autoreload=True
)