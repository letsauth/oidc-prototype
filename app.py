#!/usr/bin/env python3

from flask import Flask, render_template
from jwkest.jwk import jwk_wrap, RSA


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

    # FIXME: Put this bit somewhere useful / reusable.
    print("Generating ephemeral keypair...")
    keypair = RSA.generate(2048)
    pubjwk = jwk_wrap(keypair).serialize()
    print(pubjwk)

    ip, port = "127.0.0.1", 5000
    if len(sys.argv) > 1:
        ip = sys.argv[1]
        if len(sys.argv) > 2:
            port = int(sys.argv[2])
    app.run(ip, port)


if __name__ == "__main__":
    main()
