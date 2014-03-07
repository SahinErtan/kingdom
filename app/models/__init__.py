from flask.ext.sqlalchemy import SQLAlchemy
from .. import app


db = SQLAlchemy(app)


from . import db_helpers
from . import friends
from . import games
from . import users
