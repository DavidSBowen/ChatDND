# Getting Started
Getting started
1. Use the Remote Development extention for VSCode, the environment will be set up as a docker container
or...
1. [Install Poetry](https://python-poetry.org/docs/#installation)
1. Make sure you're in the api directory `cd api`
1. Install all python depentencies with `poetry install`

# Running the API
1. Make sure you're in the api folder, `cd api`
1. Activate the python virtualenv with `poetry shell`
1. Run the server with `uvicorn api.main:app --reload`