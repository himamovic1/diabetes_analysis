from flask import render_template
from flask_classful import FlaskView


class HomeView(FlaskView):
    """ Home page view class """
    _templates = {
        'main': 'home.html'
    }

    def main(self):
        template = self._templates['main']
        return render_template(template)
