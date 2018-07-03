from uuid import uuid4

from sqlalchemy.orm import relationship

from bss_diabetes.extensions import database as db
from bss_diabetes.models.core import Model


class DailySample(Model):
    __tablename__ = 'daily_sample'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    value = db.Column(db.Integer, nullable=False)

    # def __init__(self, date, time, code, value):
    #     self.date = date
    #     self.time = time
    #     self.code = code
    #     self.value = value

    @classmethod
    def from_string(cls, line):
        data = line.rstrip().lstrip().split('\t')

        try:
            return cls(*data)
        except (IndexError, TypeError) as e:
            return None

    def to_dict(self):
        return {
            'date': self.date,
            'time': self.time,
            'code': self.code,
            'value': self.value,
        }


class Patient(Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, primary_key=True)
    samples = relationship("DailySample")

    # def __init__(self):
    #     self.id = str(uuid4())
    #     self.samples = None
    #
    #     self.pre_breakfast = 0.0
    #     self.post_breakfast = 0.0
    #     self.pre_lunch = 0.0
    #     self.post_lunch = 0.0
    #     self.pre_supper = 0.0
    #     self.post_supper = 0.0

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            rows = f.readlines()

        raw_samples = [Sample.from_string(r) for r in rows]

        subject = cls()
        subject.samples = [s for s in raw_samples if s is not None]
        return subject

    def to_dict(self):
        return {
            'id': self.id,
            'samples': [s.to_dict() for s in self.samples]
        }
