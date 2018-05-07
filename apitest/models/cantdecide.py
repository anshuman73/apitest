from sqlalchemy.types import UserDefinedType
from sqlalchemy.orm import deferred, column_property
from sqlalchemy import func, Float
from apitest import db


class EARTH(UserDefinedType):
    def get_col_spec(self, **kw):
        return 'EARTH'


class Pincodes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.UnicodeText, nullable=False)
    # defer loading, as the raw value is pretty useless in python
    earth_location = deferred(db.Column(EARTH))
    # A deferred column, aka column_property cannot be adapted, extract the
    # real column. A bit of an ugly hack.
    latitude = column_property(func.latitude(*earth_location.columns,
                                             type_=Float))
    longitude = column_property(func.longitude(*earth_location.columns,
                                               type_=Float))
