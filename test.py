from flask import Flask, render_template,url_for

app = Flask(__name__)

with app.test_request_context():
    url = url_for('static',filename='main.css')
@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/minutes")
def minutes():
  return render_template('minutes.html')



if __name__ == "__main__":
  app.run(debug=True)