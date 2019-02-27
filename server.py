from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/play/<num>')
def level1(num):
    return render_template("playground1.html", x=int(num))
    
@app.route('/play/<num>/<color>')
def level2(num, color):
    return render_template("playground2.html", y=int(num), color = color)

if __name__=="__main__":
    app.run(debug=True)