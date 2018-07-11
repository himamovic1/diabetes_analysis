from flask import render_template
from flask_classful import FlaskView

from bss_diabetes.extensions import database


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
        from bss_diabetes.extensions import database
        result_set = database.engine.execute("""
            select ds.code, list.code, avg(ds.value)
            from daily_sample ds, (
                select distinct tmp.patient_id as pid, tmp.code as code
                from daily_sample tmp
                where tmp.code in (66, 67, 68)
                order by tmp.code
            ) as list
            where ds.patient_id = list.pid
            group by ds.code, list.code
            having ds.code in (58, 59, 60, 61, 62, 63)
            order by ds.code, list.code;
        """)

        diet_habits = {
            66: [],
            67: [],
            68: [],
        }

        for row in result_set:
            diet_habits[row[1]].append(str(row[2]))

        template = self._templates['diet']
        return render_template(template,
                               bellow_avg=diet_habits[66],
                               avg=diet_habits[67],
                               above_avg=diet_habits[68])

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
