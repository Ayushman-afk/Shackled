from pyscript import when, display







@when("click", "#mainscreensettings")
def settings():
    display("Working")


