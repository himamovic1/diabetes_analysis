from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
debug_toolbar = DebugToolbarExtension()
database = SQLAlchemy()
