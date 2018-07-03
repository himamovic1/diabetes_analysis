from flask import Flask

from bss_diabetes.extensions import *


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    register_extensions(app)
    register_blueprints(app)
    register_app_routes(app)

    return app


def register_extensions(app):
    """ Registers app level extensions """
    bootstrap.init_app(app)
    debug_toolbar.init_app(app)
    database.init_app(app)


def register_blueprints(app):
    from bss_diabetes.mods.home.views import HomeView

    HomeView.register(app)


def register_app_routes(app):
    """ Registers routes attached directly to the app class """
    from flask import redirect, url_for

    @app.route('/')
    def root():
        return redirect(url_for('HomeView:main'))


def post_boot(app):
    """ Defines actions triggered after application boot """
    pass
