from models import Students


def getUser(email):
    return Students.query.filter_by(email=email).first()


def getAllDetails():
    return Students.query.all()
