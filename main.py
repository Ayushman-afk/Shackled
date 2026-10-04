from pyscript import when, display, document

@when("click", "#mainscreenplay")
def start():
    playscreen = document.getElementById("playscreen")
    playscreen.style.display = "block"
    playscreen.style.display = "flex"

@when("click", "#mainscreensettings")
def settings():
    display("Working")