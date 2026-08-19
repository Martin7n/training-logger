from extensions import db

class BookModel(db.Model):
    __tablename__ = 'books'
    pk = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    title = db.Column(db.String)

    def __repr__(self):
        return f'No {self.pk}: {self.title} from {self.author}'

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}


class ReaderModel(db.Model):
    __tablename__ = 'readers'
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'No {self.pk}: {self.name}'

