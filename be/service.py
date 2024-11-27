import string
import random
from models import URL
from __init__ import db


class Service:
    def get_short_code(self, long_url):
        url = URL.query.filter_by(long_url=long_url).first()
        return url.short_code if url else None

    def get_long_url(self, short_code):
        return URL.query.filter_by(short_code=short_code).first().long_url

    def create_short_code(self, long_url):
        short_code = self.generate_short_code()

        new_url = URL(short_code=short_code, long_url=long_url)
        db.session.add(new_url)
        db.session.commit()

        return short_code

    def generate_short_code(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
