import json
from operator import and_

from flask import render_template
from flask_classful import FlaskView
from bss_diabetes.extensions import database
from sqlalchemy import func

from bss_diabetes.models.patient import DailySample


class HomeView(FlaskView):
    """ Home page view class """
    _templates = {
        'main': 'home.html',
        'activity': 'graphs/activity.html',
        'diet': 'graphs/diet.html',
        'age': 'graphs/age.html',
        'smoking': 'graphs/smoking.html'
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

    def age(self):
        template = self._templates['age']

        data_set = database.engine.execute(
            """ SELECT CASE WHEN AGE < 30 THEN '30' 
                            WHEN AGE BETWEEN 30 AND 40 THEN '30 - 40'
                            WHEN AGE BETWEEN 40 AND 50 THEN '40 - 50'
                            WHEN AGE BETWEEN 50 AND 60 THEN '50 - 60'
                            WHEN AGE > 60 THEN '60' 
                            END AS CAT, COUNT(*) AS NUM
                FROM PATIENT_DATA
                WHERE AGE IS NOT NULL AND FBS = 1
                group by CAT
                order by CAT""")

        data = [row for row in data_set]

        data_labels = [row[0] for row in data]
        data_values = [row[1] for row in data]

        return render_template(template, data_labels=data_labels, data_values=data_values)

    def smoking(self):
        template = self._templates['smoking']

        data_set = database.engine.execute(
            """
            select fbs, count(*) 
            from patient_data 
            where years_as_smoker is not null and years_as_smoker > 1 and fbs is not null
            group by fbs
            """)

        data = [row for row in data_set]

        data_values = [row[1] for row in data]

        return render_template(template, data_values=data_values)
