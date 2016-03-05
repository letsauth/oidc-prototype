#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from flask import Flask, render_template
from jose import jwk


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

    # FIXME: Put these somewhere useful / reusable.
    print("Generating ephemeral keypair...")
    keypair = RSA.generate(2048)
    seckey = keypair.exportKey()
    pubkey = keypair.publickey().exportKey()

    print(seckey.decode('utf-8'))
    print(pubkey.decode('utf-8'))

    # The jose library doesn't yet support serializing RSA keys as JWKs
    # We'll have to do it ourselves
    # See https://tools.ietf.org/html/rfc7518#section-6.3
    # Each key object has an `n` and `e` property that we just need to encode
    # Just have to base64url encode each value as an unsigned big-endian octect
    # sequence

    ip, port = "127.0.0.1", 5000
    if len(sys.argv) > 1:
        ip = sys.argv[1]
        if len(sys.argv) > 2:
            port = int(sys.argv[2])
    app.run(ip, port)


if __name__ == "__main__":
    main()
