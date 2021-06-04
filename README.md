## Flask Application with sqlite3

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Installation

application requires [Python](https://www.python.org/) 3.8 to run.

Install the dependencies and devDependencies and start the server.

```sh
export FLASK_ENV=development
cd portfolio-arunthomasalex
pip install -r requirements.txt
flask init-db
pytest
gunicorn app:app
```

For production environments(Heroku)...

```sh
flask init-db
```
## License

MIT

**Free Software, Hell Yeah!**
