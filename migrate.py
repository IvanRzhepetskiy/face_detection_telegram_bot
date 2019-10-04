import os
import sys
from time import sleep

def create_venv():
    #creates venv with pip
    print("###Setting up a virtual environment")
    os.system("virtualenv .venv")
    print("###Activating venv")
    sleep(1)
    activate_this = ".venv/bin/activate_this.py"
    exec(open(activate_this).read(), {'__file__': activate_this})
    if sys.prefix == sys.base_prefix:
        print("###Venv wasn't activated")
        exit()
    print("###Installing packages")
    os.system("pip install -r requirements.txt")

if __name__ == "__main__":
    create_venv()
    