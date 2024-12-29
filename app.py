from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/legacy')
def legacy():
    return render_template('legacy.html')

@app.route('/mbc')
def mbc():
    return render_template('mbc.html')

@app.route('/mbc/speed')
def mbc_speed():
    return render_template('mbc_speed.html')

@app.route('/mbc/traditional')
def mbc_traditional():
    return render_template('mbc_traditional.html')

@app.route('/mbc/flair')
def mbc_flair():
    return render_template('mbc_flair.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/entry')
def entry():
    return render_template('entry.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)