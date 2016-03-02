from flask import Flask


# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


class AuthException(Exception):
	pass


@app.errorhandler(404)
def hard_404(error):
	return render_template("404.html"), 404


@app.route("/")
def index():
	return render_template("hello.html", text="Hello world")


def main():
	import sys

	ip, port = "127.0.0.1", 5000
	if len(sys.argv) > 1:
		ip = sys.argv[1]
		if len(sys.argv) > 2:
			port = int(sys.argv[2])
	app.run(ip, port)


if __name__ == "__main__":
	main()