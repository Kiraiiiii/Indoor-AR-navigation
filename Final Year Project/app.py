from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('front.html')

@app.route('/index1.html',methods=["POST"])
def login():
    if request.method == 'POST':
        return redirect("https://foamy-thankful-marscapone.glitch.me/")

if __name__ == '__main__':
    app.run(debug=True)
