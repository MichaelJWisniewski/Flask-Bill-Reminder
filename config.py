import os

basedir = os.path.dirname(os.path.abspath(__file__)) 

class Config:
  SECRET_KEY = b'M\\\xbc\xf0\x85\xe9\xaa\xee-\xe0QG\xb8\xba|\xb3|\xd6.\xf5\x8f\xf5\xda\xb9'
  SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'app.db')}"
  SQLALCHEMY_TRACK_MODIFICATIONS = False