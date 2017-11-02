# Echo
DAPME Fall 2017

## First Time Setup
1. Ensure that you have Python 2.7
2. Install your Virtual Envitonment 
	```$ pip install virtualenv ```
3. Create virtual enviornment
	```$ virtualenv . ```
4. Enter virtual environment 
	```$source bin/activate ```
5. Install all dependencies
	```(BusyBee)$ pip install -r requirements.txt ```
6. To exit virtualenv
	```$ deactivate ```

### And finally:
Run script. 
```$ python run.py```


## About Echo
* Built in [Flask](http://flask.pocoo.org/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) is used to interface with a SQL database.
* Continuous Integration with Travis