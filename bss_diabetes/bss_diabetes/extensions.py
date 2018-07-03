from flask_assets import Environment
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
asset_environment = Environment()
debug_toolbar = DebugToolbarExtension()
database = SQLAlchemy()
