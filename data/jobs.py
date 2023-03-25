import datetime
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))

    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)

    collaborators = sqlalchemy.Column(sqlalchemy.String)

    start_date = sqlalchemy.Column(sqlalchemy.String, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.String, default=None)

    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    user = orm.relationship('User', backref='posts')
