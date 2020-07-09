from application import db
  
class Stance(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    stance = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return ''.join([
            "Stance ID", str(self.id), '\r\n'
            "Stance", str(self.stance), '\r\n'
        ])
