from flask import render_template
from flask_classful import FlaskView


class HomeView(FlaskView):
    """ Home page view class """
    _templates = {
        'main': 'home.html',
        'activity': 'graphs/activity.html',
        'diet': 'graphs/diet.html',
    }

    def main(self):
        template = self._templates['main']
        return render_template(template)

    def activity(self):
        template = self._templates['activity']
        return render_template(template)

    def diet(self):
        template = self._templates['diet']
        return render_template(template)
