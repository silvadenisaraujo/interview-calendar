from service import db


class Interviewer(db.Model):
    __tablename__ = 'interviewer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    department = db.Column(db.String(140))

    def __repr__(self):
        return '<Interviewer {}>'.format(self.name)

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Interviewer.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Interviewee(db.Model):
    __tablename__ = 'interviewee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    linked_in = db.Column(db.String(140))
    email = db.Column(db.String(140))

    def __repr__(self):
        return '<Interviewee {}>'.format(self.name)

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Interviewee.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Interview(db.Model):
    __tablename__ = 'interview'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    # One to One
    interviewer = db.Column(db.Integer, db.ForeignKey('interviewer.id'))
    # One to One
    interviewee = db.Column(db.Integer, db.ForeignKey('interviewee.id'))

    def __repr__(self):
        return '<Interview {}>'.format(self.id)

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Interviewes.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
