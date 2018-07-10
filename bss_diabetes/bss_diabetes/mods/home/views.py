import json
from operator import and_

from flask import render_template
from flask_classful import FlaskView
from sqlalchemy import func

from bss_diabetes.models.patient import DailySample


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
        # active = [str(n[0]) for n in
        #           DailySample.query \
        #               .with_entities(func.avg(DailySample.value).label('avg')) \
        #               .filter(and_(DailySample.value.isnot(None), DailySample.code.in_((69, 70, 71)))) \
        #               .all()]

        from bss_diabetes.extensions import database
        active_set = database.engine.execute(
            """select code, avg(value) as average
                from daily_sample
                where patient_id in (select distinct patient_id from daily_sample where code in (69, 70, 71))
                group by code
                having code in (58, 59, 60, 61, 62, 63)
                order by code""")

        inactive_set = database.engine.execute(
            """select code, avg(value) as average
                from daily_sample
                where patient_id not in (select distinct patient_id from daily_sample where code in (69, 70, 71))
                group by code
                having code in (58, 59, 60, 61, 62, 63)
                order by code""")

        active = [str(row[1]) for row in active_set]
        inactive = [str(row[1]) for row in inactive_set]

        template = self._templates['activity']
        return render_template(template, active=active, inactive=inactive)

    def diet(self):
        template = self._templates['diet']
        return render_template(template)
