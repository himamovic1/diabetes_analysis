from bss_diabetes.application import app
from bss_diabetes.extensions import database as db

from bss_diabetes.models.patient import DailySample, Patient
from bss_diabetes.models.patient_data import PatientData


def seed_patients():
    from glob import glob
    import os

    pattern = os.path.join('Diabetes-Data', 'data-*')
    files = [f"{name}" for name in glob(pattern)]

    for f in files:
        Patient.from_file(f).save()


def seed_patient_data():
    from glob import glob
    import os

    pattern = os.path.join('Heart-Disease-Data/processed-data', '*.data')
    files = [f"{name}" for name in glob(pattern)]

    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            rows = f.readlines()

        for r in rows:
            PatientData.from_string(r).save()


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
        seed_patients()
        seed_patient_data()

        db.session.commit()
        print("All done, enjoy mate :)")
