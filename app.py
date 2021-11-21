from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)
'''
@app.route('/index')
def index():
    user = { 'nickname': 'Александр' } # выдуманный пользователь
    return render_template("index.html",
        title = 'Home',
        user = user)
'''
@app.route('/index')
def show_form():
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def show_result():
    result = request.form
    return render_template('result.html', result=result)

if __name__ == "__main__":
     app.run()

