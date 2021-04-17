from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#   __tablename__ = 'users'
#   id = db.Column(db.String(22), primary_key=True)
#   username = db.Column(db.String(50), nullable=False)
#   url = db.Column(db.String(100), nullable=False)
#   created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

#   @classmethod
#   def create(cls, username, base_url):
#     # print('DEntro de create', base_url)
#     user_id = b64encode(username.encode()).decode('utf-8')
#     url = base_url + f'/artists/{user_id}'
#     user = User(id=user_id, username=username, url=url)
#     return user.save()

#   def save(self):
#     try:
#       db.session.add(self)
#       db.session.commit()
#       return self
#     except:
#       return False

#   def update(self):
#     self.save()

#   def delete(self):
#     try:
#       db.session.delete(self)
#       db.session.commit()
#       return True
#     except:
#       return False

#   def json(self):
#     print(self.id, self.username, self.created_at)
#     return {
#       'id': self.id,
#       'username': self.username,
#       'created_at': self.created_at,
#       'url': self.url,
#       }
