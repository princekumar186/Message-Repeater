from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        message = request.form["message"]
        count = int(request.form["count"])
        output = "\n".join([message] * count)
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
