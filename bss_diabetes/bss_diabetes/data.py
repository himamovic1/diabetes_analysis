from uuid import uuid4


class Sample:

    def __init__(self, date, time, code, value):
        self.date = date
        self.time = time
        self.code = code
        self.value = value

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


class Patient:

    def __init__(self):
        self.id = str(uuid4())
        self.samples = None

        self.pre_breakfast = 0.0
        self.post_breakfast = 0.0
        self.pre_lunch = 0.0
        self.post_lunch = 0.0
        self.pre_supper = 0.0
        self.post_supper = 0.0

    def process(self):
        counter = {
            'pre_breakfast': 0,
            'post_breakfast': 0,
            'pre_lunch': 0,
            'post_lunch': 0,
            'pre_supper': 0,
            'post_supper': 0
        }

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


if __name__ == '__main__':
    from glob import glob
    import os

    pattern = os.path.join(os.pardir, 'Diabetes-Data', 'data-*')
    files = [f"{name}" for name in glob(pattern)]

    patients = [Patient.from_file(f) for f in files]
    raw_patients = [p.to_dict() for p in patients]

    import json

    data = json.dumps(raw_patients)
    print('-' * 20)
    print(data)
    print('-' * 20)
