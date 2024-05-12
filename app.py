from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('test.html')


@app.route('/bin_one')
def return_bin_one():  # put application's code here
    return render_template('bin_one.html')


@app.route('/bin_two')
def return_bin_two():
    return render_template('bin_two.html')


if __name__ == '__main__':
    app.run()
