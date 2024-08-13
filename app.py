from flask import Flask

#__name__.=main
app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello Word"

@app.route("/about")
def about():
    return "pagina sobre"


if __name__ == "__main__":
    app.run(debug=True)