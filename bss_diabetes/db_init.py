from bss_diabetes.application import app
from bss_diabetes.extensions import database as db

from bss_diabetes.models.patient import DailySample, Patient

if __name__ == '__main__':

    with app.app_context():
        ctx = app.test_request_context('/')
        ctx.push()

        print("DATABASE: " + app.config.get('SQLALCHEMY_DATABASE_URI'))
        ans = input("Do you want to destroy existing database and create new database? ")

        if ans not in ('Y', 'y'):
            exit()

        print("Nuking the database...")
        db.drop_all()

        print("Rebuilding the database...")
        db.create_all()

        # Adding seed data to session
        print('And the Lord said "Let there be data".')
        # seed(db)

        db.session.commit()
        print("All done, enjoy mate :)")
