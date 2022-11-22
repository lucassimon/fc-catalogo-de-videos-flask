import datetime
import uuid


from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from apps.database import db


def generate_uuid():
    return uuid.uuid4()


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # id = db.Column(db.String(255), name="uuid", primary_key=True, default=generate_uuid)
    title = db.Column(db.String(255))
    slug = db.Column(db.String(255), unique=True)
    description = db.Column(db.Text())
    status = db.Column(db.Integer)
    is_deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
