import pystray
from pystray import MenuItem as item
import PIL.Image
import subprocess
from pathlib import Path
import os
import sys

script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
os.chdir(script_dir)
os.environ['PYSTRAY_BACKEND'] = 'gtk'

image = PIL.Image.open("keyboard.png")

profiles_folder = ("profiles/")
files = sorted(list(profiles_folder.iterdir()))

def on_clicked(text):
    subprocess.run(["xmodmap", str(text)])
    icon.notify(f"{text} was selected")

def create_menu():
    menu_items = []
    menu_items.append(item("select you profile", lambda icon, item: icon.remove_notification()))
    for file in files:
        menu_items.append(item(str(file), lambda item, text=file: on_clicked(text))) 
    menu_items.append(item("close", lambda item: icon.stop()))
    return pystray.Menu(*menu_items)

icon = pystray.Icon("xmodmapProfiler", image, menu=create_menu())

icon.run()
