from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')
# http:// 192.168.3.8:5000

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)