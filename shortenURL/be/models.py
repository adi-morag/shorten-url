from __init__ import db


class URL(db.Model):
    __tablename__ = 'urls'

    short_code = db.Column(db.String(10), unique=True,
                           nullable=False, primary_key=True)
    long_url = db.Column(db.String(4096), nullable=False)

    # def __repr__(self):
    #     return f'{self.short_code}: {self.long_url}'
