from pyscript import when, display, document
from flask import Flask, render_template



@when("click", "#test_button")
def test_button():
    test_button = display

@when("click", "#mainscreensettings")
def settings():
    display("Working")






app = Flask(__name__)
#creates a flask application object
#name is the special object that tells flask where to look for your resources like the HTML code

@app.route('/') #- is a decorator. tells flask whenever the user visits the root url, it should run the new_window function
def new_window():
    return render_template('index.html') # render_template tells flask to look inside a folder called templates/ find a file called index.html and send that web page to the user's browser.

if __name__ == '__main__': #- ensures it is only run when if the script is executed directly.
    app.run(debug=True) #- debug = tru
