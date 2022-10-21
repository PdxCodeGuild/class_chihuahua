from flask import Flask, render_template

app = Flask(__name__)
app.debug=True

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("burrito_template.html")
        
if __name__ == '__main__':
    app.run()