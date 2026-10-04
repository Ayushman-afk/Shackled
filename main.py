from pyscript import when, display

@when("click", "#mainscreenplay")
def start():
    display("Working")
@when("click", "#mainscreensettings")
def settings():
    display("Working")