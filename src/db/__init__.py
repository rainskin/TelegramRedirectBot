from loader import db
from .users import Users
from .service import Service
from .ref_links import RefLinks


users = Users(db)
service = Service(db)
ref_links = RefLinks(db)
