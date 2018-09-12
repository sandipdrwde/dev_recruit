from datetime import datetime
from app import db

class ApplicationDetail(db.Model):
    __tablename__ = 'ApplicationDetail'
    applicant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(60), nullable=False)
    mobile_number = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(60), nullable=True)
    pincode = db.Column(db.String(10), nullable=True)

    notice_period = db.Column(db.String(20), nullable=False)
    experience = db.Column(db.String(20), nullable=False)
    current_ctc = db.Column(db.String(25), nullable=False)
    expected_ctc = db.Column(db.String(25), nullable=False)
    upload_file = db.Column(db.BLOB, nullable=False)
    created_dt = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Applicant {}>'.format(self.first_name)


class ApplicationStatus(db.Model):
    __tablename__ = 'ApplicationStatus'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey('ApplicationDetail.applicant_id'))
    status = db.Column(db.String(140))
    created_dt = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Status {}>'.format(self.status)
