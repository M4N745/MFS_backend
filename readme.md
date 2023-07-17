    Creating virtualenv:

`virtualenv venv --python=python3.10.7`

    Activating virtualenv:

`source venv/bin/activate`

    installing required packages (in virtualenv):

`pip install -r packages.txt`

    Migrate tables (in virtualenv):

`flask db upgrade`

    Starting local server (in virtualenv):

`flask run`


