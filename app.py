from flask import Flask, render_template
import k

app = Flask(__name__)


@app.route("/")
def index():
    headlines, error = k.fetch_headlines()
    return render_template("index.html", headlines=headlines, error=error)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
