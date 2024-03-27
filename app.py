from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def render_index():
    return render_template('index.html')



@app.route('/register', methods=['POST'])
def render_register():
    return render_template('registrationLk.html')

@app.route('/authenticate', methods=['POST'])
def render_auth():
    return render_template('loginLk.html')

@app.route('/lk', methods=['GET'])
def render_lk():
    return render_template('lk.html')

if __name__ == '__main__':
    app.run()
