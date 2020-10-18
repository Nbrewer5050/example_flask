# Flask tutorial web app
This repository hosts the app we've worked on during previous classes.
It is not actually an online store despite the name, a lot of this code was written during a live session
so it is not the cleanest.

## Installing
You should have a virtual environment somewhere on your machine that you'd like to use for this project
prior to setting it up.
In our case, our virtual environment was in the parent directory of wherever we had this project's folder or directory.

So in our case, from this folder we would run:
`source ../venv/bin/activate`

Now we want to install our python modules via pip3, so run:
`pip3 install -r requirements.txt`

Finally to run the project:
`export FLASK_APP=store.py`

Optionally:
`export FLASK_DEBUG=1`

Then:
`flask run`

Remember that to deactivate your virtual environment we'd just type:
`deactivate`