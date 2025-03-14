## Nota: Por alguna razón no puedo abrir mi cuenta y se guardan los commits como Raquel-Reyes
## Realizado por Karen Reyes

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
