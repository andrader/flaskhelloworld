from flask import Flask
from flask import jsonify

application = Flask(__name__)


@application.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    
    page = fr"""
    <html>
    <h1>Hello</h1>
    
    <p>
        Continuous Delivery Demo. 
        <br><br>
        Change de route to url/echo/meunome
    </p>
    
    <p>
        Check out this <a href="/echo/MYNAMEHERE">example</a>
    </p>
    
    </html>
    """
    return page


@application.route("/echo/<name>")
def echo(name):
    print(f"This was placed in the url: echo/{name}")
    page = fr"""
    <html>
    <h1>Hello</h1>
    
    <p>
        Hello <b>{name}</b>
    </p>
    
    <p>
        <a href="/">Back</a>
    </p>
    
    </html>
    """
    return page


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()