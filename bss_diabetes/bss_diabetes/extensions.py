from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_webpack import Webpack

bootstrap = Bootstrap()
debug_toolbar = DebugToolbarExtension()
database = SQLAlchemy()
webpack = Webpack()
