import subprocess
from listener import listen

def run_droid():
    text = listen()
    if text:
        subprocess.run(['speaker.exe'], input=text.encode())
