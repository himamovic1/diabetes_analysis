def PatientData:
    __tablename__ = 'patient_data'

    id = db.Column(db.Integer,  primary_key=True)

    age = db.Column(db.Integer, unique=False, nullable=True)
    sex = db.Column(db.Integer, unique=False, nullable=True)
    resting_blood_sugar = db.Column(db.Integer, unique=False, nullable=True)
    smoking = db.Column(db.Integer, unique=False, nullable=True)
    cigs_per_day = db.Column(db.Integer, unique=False, nullable=True)
    years_as_smoker = db.Column(db.Integer, unique=False, nullable=True)
    fbs = db.Column(db.Integer, unique=False, nullable=True)
    diabetes_history = db.Column(db.Integer, unique=False, nullable=True)
    num = db.Column(db.Integer, unique=False, nullable=True)


    def __init__(self, age, sex, resting_blood_sugar, smoking, cigs_per_day, years_as_smoker, fbs, diabetes_history, num ):
        self.age = age
        self.sex = sex
        self.resting_blood_sugar = resting_blood_sugar
        self.smoking = smoking
        self.cigs_per_day = cigs_per_day
        self.years_as_smoker = years_as_smoker
        self.fbs = fbs
        self.diabetes_history = diabetes_history
        self.num = num

