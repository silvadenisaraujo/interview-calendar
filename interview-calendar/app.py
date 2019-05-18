from flask import Flask

app = Flask(__name__)

@app.route('/slots')
def slots():
    return ""

if __name__ == '__main__':
    app.run(debug=True)
