# Harvest Finance Metrics Broadcaster

This is a script to gather key metrics from the harvest.finance ecosystem and produce content to share with the community.

## Setup

- Install virtualenv https://docs.python.org/3/library/venv.html
- Create virtualenv `virtualenv .venv`
- Activate virtualenv `source .venv/bin/activate`.
- Install requirements: `pip install -r requirements.txt`


## Execution

- Execute script with parameters: `python main.py 01/04/2021 09/04/2021 https://ethparser-api.herokuapp.com`

## Development

- Install requirements: `pip install -r requirements-dev.txt`
- Format code with `black .` before any commit