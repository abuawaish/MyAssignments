from flask import Flask , render_template
app = Flask(__name__)

@app.route("/home")
def input_info():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)