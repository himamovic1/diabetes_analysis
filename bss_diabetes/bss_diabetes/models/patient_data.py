from bss_diabetes.extensions import database as db
from bss_diabetes.models.core import Model
from bss_diabetes.models.utils import parse_int


class PatientData(Model):
    __tablename__ = 'patient_data'

    id = db.Column(db.Integer, primary_key=True)

    age = db.Column(db.Integer, unique=False, nullable=True)
    sex = db.Column(db.Integer, unique=False, nullable=True)
    resting_blood_pressure = db.Column(db.Integer, unique=False, nullable=True)
    smoking = db.Column(db.Integer, unique=False, nullable=True)
    cigs_per_day = db.Column(db.Integer, unique=False, nullable=True)
    years_as_smoker = db.Column(db.Integer, unique=False, nullable=True)
    fbs = db.Column(db.Integer, unique=False, nullable=True)
    diabetes_history = db.Column(db.Integer, unique=False, nullable=True)
    num = db.Column(db.Integer, unique=False, nullable=True)

    def __init__(self, age, sex, resting_blood_pressure, smoking, cigs_per_day,
                 years_as_smoker, fbs, diabetes_history, num):

        self.sex = parse_int(sex)
        self.age = parse_int(age)
        self.resting_blood_pressure = parse_int(resting_blood_pressure)
        self.smoking = parse_int(smoking)
        self.cigs_per_day = parse_int(cigs_per_day)
        self.years_as_smoker = parse_int(years_as_smoker)
        self.fbs = parse_int(fbs)
        self.diabetes_history = parse_int(diabetes_history)
        self.num = parse_int(num)

    @classmethod
    def from_string(cls, line):
        data = line.rstrip().lstrip().split(',')

        try:
            return cls(*data)
        except (IndexError, TypeError) as e:
            return None

    def to_dict(self):
        return {
            'id': self.id,
            'age': self.age,
            'sex': self.sex,
            'resting_blood_pressure': self.resting_blood_pressure,
            'smoking': self.smoking,
            'cigs_per_day': self.cigs_per_day,
            'years_as_smoker': self.years_as_smoker,
            'fbs': self.fbs,
            'diabetes_history': self.diabetes_history,
            'num': self.num
        }
