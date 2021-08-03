from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__, template_folder="./templates")

@app.route("/")
def hello_world():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(port=5000)