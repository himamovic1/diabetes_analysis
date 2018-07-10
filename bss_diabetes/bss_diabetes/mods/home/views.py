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
