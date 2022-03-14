# Boilerplate
import os

# Get script path
current_path = os.path.realpath(__file__)
new_path = current_path.replace(r'About.Panel\Sources.stack\pyRoovit.pushbutton\script.py','')

# try to open path
try:
    os.startfile(new_path)
except:
    print('The path was not found.')