from pyscript import when, display, document

from flask import Flask, render_template



@when("click", "#test_button")
def test_button():
    test_button = display

@when("click", "#mainscreensettings")
def settings():
    display("Working")


app = Flask(__name__)

@app.route('/')
def new_window():
    return render_template('index.html')
app.run()
