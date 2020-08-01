# onefit : Fitness Tracker/Logger/Planner
django backend with (planned) react frontend

# Installation:
- Clone the repository on your machine
- Get a secret key off djecrety.io and add it to your environment variables under 'ONEFIT_SECRET_KEY'
    - This can be done in linux bad adding `export ONEFIT_SECRET_KEY=****` in your .bashrc, 
        where **** is the key from djecrety.io
- Install python3 on your machine, and open up a terminal in the repository directory
- Create and activate a virtualenvironment in the base of the repository: `python3 -m venv .venv`
    - activate the virtualenv by sourcing the script: `. ./.venv/bin/activate` or `source ./.venv/Scripts/activate`
    - This must be done everytime you use a new terminal; IDE's like VSCode will automatically source them for you
    - You can tell you're in a virtualenv because you will see `(.venv)` in the terminal line
- Install dependencies: `pip install -r requirements.txt`
### You should now be fully installed!
You can start the django project by navigating into the project directory and run `python3 manage.py runserver` which start the site; you can access it by navigating to `localhost:8000` in your browser.

# Admin:
The default login info is `admin`, the password is `onefit`