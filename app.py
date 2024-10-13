from flask import Flask, redirect, url_for, session
from flask import render_template_string, request

app = Flask(__name__)
app.secret_key = "dev"  # Required for session handling in Flask

# HTML template with counter display and buttons
html_template = """
<!doctype html>
<html>
    <head>
        <title>Simple Counter App</title>
    </head>
    <body>
        <h1>Counter Application - Devops</h1>
        <p>Counter Value: {{ counter }}</p>
        <form action="/increment" method="post">
            <button type="submit">Increment</button>
        </form>
        <form action="/decrement" method="post">
            <button type="submit">Decrement</button>
        </form>
        <form action="/reset" method="post">
            <button type="submit">Reset</button>
        </form>
    </body>
</html>
"""

@app.route("/")
def home():
    counter = session.get("counter", 0)
    return render_template_string(html_template, counter=counter)

@app.route("/increment", methods=["POST"])
def increment():
    session["counter"] = session.get("counter", 0) + 1
    return redirect(url_for("home"))

@app.route("/decrement", methods=["POST"])
def decrement():
    session["counter"] = session.get("counter", 0) - 1
    return redirect(url_for("home"))

@app.route("/reset", methods=["POST"])
def reset():
    session["counter"] = 0
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
