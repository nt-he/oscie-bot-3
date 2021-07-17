from bot import db
class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    discord_id = db.Column(db.Integer, nullable=False)
    strikes = db.Column(db.Integer, default=0)
    muted = db.Column(db.Boolean, default=False)
    guild = db.Column(db.Integer)
        
class CachedUser(db.Model):
    __tablename__ = "cached_users"
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    username = db.Column(db.String(32), nullable=True)
    discriminator = db.Column(db.String(4), nullable=True)