from application import db
  
class Trick(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    trick = db.Column(db.String(25), nullable = False)

    def __repr__(self):
        return ''.join([
            "Trick ID", str(self.id), '\r\n'
            "Trick", str(self.stance), '\r\n'
        ])
